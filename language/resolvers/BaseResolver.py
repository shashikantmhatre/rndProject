from language.context.ContextManager import ContextManager
from language.context.DataType import DataType
from language.resolvers.ResolverRegistry import ResolverRegistry


class BaseResolver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseResolver, cls).__new__(cls)
            cls._instance.register()
        return cls._instance

    def resolve(self, ctx, contextmanager:ContextManager) -> DataType:
        """
        resolve the dsl expression
        """
        raise NotImplementedError()

    def getname(self):
        """
        resolve the dsl expression
        """
        raise NotImplementedError()

    def register(self):
        ResolverRegistry().register(self.getname().lower(), self)
