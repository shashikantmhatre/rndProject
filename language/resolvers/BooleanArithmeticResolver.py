from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class BooleanArithmeticResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.BooleanArithmeticContext, contextmanager):
        return ResolverRegistry().get(ctx.arithmeticExp().__class__.__name__).resolve(ctx.arithmeticExp(), contextmanager)

    def getname(self):
        return ExprParser.BooleanArithmeticContext.__name__
