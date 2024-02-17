from antlr.generated.ExprParser import ExprParser
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class GetFunctionResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.GetFunctionContext, memory):
        ret_value = ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(), memory)
        cnt = 0
        if ctx.INT() is not None:
            cnt = int(ctx.INT().getText())

        if isinstance(ret_value,list):
            if len(ret_value) > cnt:
                return ret_value[cnt]
            else:
                return None

        return ret_value

    def getname(self):
        return ExprParser.GetFunctionContext.__name__
