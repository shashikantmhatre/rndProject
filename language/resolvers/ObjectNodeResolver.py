from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.resolvers.BaseResolver import BaseResolver


class ObjectNodeResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.ObjectNodeContext, memory):
        return Data({})

    def getname(self):
        return ExprParser.ObjectNodeContext.__name__
