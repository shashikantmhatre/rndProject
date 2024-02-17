from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class StatResolver(BaseResolver):
    def resolve(self, ctx: ExprParser.StatContext, contextmanager):
        n = ctx.getChildCount()
        for i in range(n):
            child = ctx.getChild(i)
            return_value = ResolverRegistry().get(child.__class__.__name__).resolve(child, contextmanager)
            if return_value is not None:
                return return_value
        return None

    def getname(self):
        return ExprParser.StatContext.__name__
