from antlr.generated.ExprParser import ExprParser
from language.context.Data import Data
from language.resolvers.BaseResolver import BaseResolver


class ListNodeResolver(BaseResolver):
    def resolve(self, ctx:ExprParser.ListNodeContext, contextmanager):
        return Data([])

    def getname(self):
        return ExprParser.ListNodeContext.__name__
