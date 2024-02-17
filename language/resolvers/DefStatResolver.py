from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class DefStatResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.DefStatContext, contextmanager):
        for i in range(len(ctx.variable())):
            ResolverRegistry().get(ctx.variable(i).__class__.__name__).resolve(ctx.variable(i), contextmanager)

    def getname(self):
        return ExprParser.DefStatContext.__name__
