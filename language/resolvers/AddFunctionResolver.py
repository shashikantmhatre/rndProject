from antlr.generated.ExprParser import ExprParser
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class AddFunctionResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.AddFunctionContext, contextmanager):
        ret_value = ResolverRegistry().get(ctx.node().__class__.__name__).resolve(ctx.node(), contextmanager)

        id = ctx.ID().getText()
        variable = contextmanager.getmemory().get(id)
        if variable is not None:
            # TODO we need to handle all the variable assignments
            if variable.gettype() == DataType.LIST:
                if ret_value is not None:
                    variable.getvalue().append(ret_value.getvalue())
            else:
                print(f'we got the {type(ret_value)} in the return')
        return None

    def getname(self):
        return ExprParser.AddFunctionContext.__name__
