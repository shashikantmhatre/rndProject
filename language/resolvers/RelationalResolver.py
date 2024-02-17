from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class RelationalResolver(BaseResolver):
    def resolve(self, ctx: ExprParser.RelationalExpContext, memory):
        left = ResolverRegistry().get(ctx.booleanExp(0).__class__.__name__).resolve(ctx.booleanExp(0), memory)
        right = ResolverRegistry().get(ctx.booleanExp(1).__class__.__name__).resolve(ctx.booleanExp(1), memory)

        if left is None or right is None:
            return Data(None)

        if ctx.op.text == '<':
            return Data(left.getvalue() < right.getvalue())
        elif ctx.op.text == '<=':
            return Data(left.getvalue() <= right.getvalue())
        elif ctx.op.text == '>':
            return Data(left.getvalue() > right.getvalue())
        elif ctx.op.text == '>=':
            return Data(left.getvalue() >= right.getvalue())
        elif ctx.op.text == '=':
            return Data(left.getvalue() == right.getvalue())
        elif ctx.op.text == '<>':
            return Data(left.getvalue() != right.getvalue())

        raise NotImplementedError(f'Relational Operator {ctx.op.text} not implemented')

    def getname(self):
        return ExprParser.RelationalExpContext.__name__
