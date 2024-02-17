from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class NodeResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.NodeContext, memory):
        if ctx.INT() is not None:
            return Data(float(ctx.INT().getText()))
        if ctx.booleanValue() is not None:
            if ctx.booleanValue().getText() == 'true':
                return Data(True)
            return Data(False)
        if ctx.STRING() is not None:
            return Data(ctx.STRING().getText().strip("\""))
        # print(ctx.getText())
        return ResolverRegistry().get(ctx.getChild(0).__class__.__name__).resolve(ctx.getChild(0), memory)

    def getname(self):
        return ExprParser.NodeContext.__name__
