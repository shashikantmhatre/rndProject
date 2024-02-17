from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class ForEachStatResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.ForeachStatContext, contextmanager):
        iter_value = []
        counter = 0
        value = ResolverRegistry().get(ctx.nodeReference().__class__.__name__).resolve(ctx.nodeReference(), contextmanager)

        if value is None:
            return None
        elif value.gettype() == DataType.NONE:
            return None
        elif value.gettype() != DataType.LIST:
            counter = 1
            iter_value = [value]
        elif value.gettype() == DataType.LIST:
            counter = len(value.getvalue())
            iter_value = self.getlist(value)

        variable = ctx.ID().getText()
        # TODO check if same variable available in context, keep it as reference
        for loop_counter in range(counter):
            contextmanager.getmemory().add(variable, iter_value[loop_counter])
            n = len(ctx.stat())
            for i in range(n):
                child = ctx.stat(i)
                return_value = ResolverRegistry().get(child.__class__.__name__).resolve(child, contextmanager)
                if return_value is not None and isinstance(return_value, Data):
                    if return_value.gettype() == DataType.BREAK:
                        break
                    elif return_value.gettype() == DataType.CONTINUE:
                        continue
                    else:
                        return return_value
        return None

    def getname(self):
        return ExprParser.ForeachStatContext.__name__

    def getlist(self, value) ->[]:
        list = []
        for val in value.getvalue():
            list.append(Data(val, value.getalias()))
        return list

