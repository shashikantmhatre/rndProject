from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class IfStatResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.IfStatContext, contextmanager):

        bool_value = ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(), contextmanager)

        if bool_value:
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
        elif ctx.elseStat() is not None:
            return ResolverRegistry().get(ctx.elseStat().__class__.__name__).resolve(ctx.elseStat(), contextmanager)

        return None

    def getname(self):
        return ExprParser.IfStatContext.__name__
