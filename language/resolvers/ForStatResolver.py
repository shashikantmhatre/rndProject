from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class ForStatResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.ForStatContext, memory):
        counter = int(ctx.INT().getText())

        variable = ctx.ID().getText()
        # TODO check if same variable available in context, keep it as reference
        for loop_counter in range(counter):
            memory[variable] = loop_counter
            n = len(ctx.stat())
            for i in range(n):
                child = ctx.stat(i)
                return_value = ResolverRegistry().get(child.__class__.__name__).resolve(child, memory)
                if return_value is not None and isinstance(return_value, Data):
                    if return_value.gettype() == DataType.BREAK:
                        break
                    elif return_value.gettype() == DataType.CONTINUE:
                        continue
                    else:
                        return return_value
        return None

    def getname(self):
        return ExprParser.ForStatContext.__name__
