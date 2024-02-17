from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class LogicalResolver(BaseResolver):
    def resolve(self, ctx: ExprParser.LogicalExpContext, contextmanager):
        left = ResolverRegistry().get(ctx.booleanExp(0).__class__.__name__).resolve(ctx.booleanExp(0), contextmanager)
        right = ResolverRegistry().get(ctx.booleanExp(1).__class__.__name__).resolve(ctx.booleanExp(1), contextmanager)

        if left is None or right is None:
            return Data(False)

        if ctx.AND() is not None:
            return Data(left.getvalue() and right.getvalue())

        return Data(left.getvalue() or right.getvalue())

    def getname(self):
        return ExprParser.LogicalExpContext.__name__
