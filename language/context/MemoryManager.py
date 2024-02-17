class MemoryManager:

    def __init__(self):
        self.memory = dict()

    def add(self, name, value):
        self.memory[name] = value

    def get(self, name):
        return self.memory.get(name)