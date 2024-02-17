from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.resolvers.BaseResolver import BaseResolver
from language.resolvers.ResolverRegistry import ResolverRegistry


class VariableResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.VariableContext, contextmanager):
        id = ctx.ID().getText()
        contextmanager.getmemory().add(id, Data(None))
        if ctx.booleanExp() is not None:
            value = ResolverRegistry().get(ctx.booleanExp().__class__.__name__).resolve(ctx.booleanExp(), contextmanager)
            contextmanager.getmemory().add(id, value)

    def getname(self):
        return ExprParser.VariableContext.__name__
