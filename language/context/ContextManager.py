from language.context.MemoryManager import MemoryManager


class ContextManager:

    def __init__(self):
        self.context = dict()
        self.memory = MemoryManager()

    def getmemory(self) -> MemoryManager:
        """

        :rtype: object
        """
        return self.memory

