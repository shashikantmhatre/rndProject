from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.context.DataType import DataType
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class MulDivResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.MulDivContext, contextmanager):
        left = ResolverRegistry().get(ctx.arithmeticExp(0).__class__.__name__).resolve(ctx.arithmeticExp(0), contextmanager)
        right = ResolverRegistry().get(ctx.arithmeticExp(1).__class__.__name__).resolve(ctx.arithmeticExp(1), contextmanager)

        if left is None or right is None:
            return Data(None)

        if left.gettype() == DataType.NONE or right.gettype() == DataType.NONE:
            return Data(None)

        if ctx.MUL() is not None:
            return Data(left.getvalue() * right.getvalue())

        return Data(left.getvalue() / right.getvalue())

    def getname(self):
        return ExprParser.MulDivContext.__name__
