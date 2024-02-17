from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class UnaryArithmeticResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.UnaryArithmeticContext, memory):
        right = ResolverRegistry().get(ctx.arithmeticExp().__class__.__name__).resolve(ctx.arithmeticExp(), memory)

        if ctx.SUB() is not None:
            return -1 * right

        return right

    def getname(self):
        return ExprParser.UnaryArithmeticContext.__name__
