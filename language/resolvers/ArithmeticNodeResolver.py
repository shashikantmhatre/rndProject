from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class ArithmeticNodeResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.ArithmeticNodeContext, contextmanager):
        return ResolverRegistry().get(ctx.node().__class__.__name__).resolve(ctx.node(), contextmanager)

    def getname(self):
        return ExprParser.ArithmeticNodeContext.__name__
