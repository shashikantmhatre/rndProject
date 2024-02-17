from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class ParenArithmeticNodeResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.ParenArithmeticContext, contextmanager):
        return ResolverRegistry().get(ctx.arithmeticExp().__class__.__name__).resolve(ctx.arithmeticExp(), contextmanager)

    def getname(self):
        return ExprParser.ParenArithmeticContext.__name__
