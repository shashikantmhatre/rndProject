from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class ParenBooleanNodeResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.ParenBooleanContext, contextmanager):
        return ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(), contextmanager)

    def getname(self):
        return ExprParser.ParenBooleanContext.__name__
