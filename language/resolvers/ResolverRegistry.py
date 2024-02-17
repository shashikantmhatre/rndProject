class ResolverRegistry:
    _registry = {}
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ResolverRegistry, cls).__new__(cls)
        return cls._instance

    def register(self, name, obj):
        self._registry[name] = obj

    def get(self, name):
        if self._registry[name.lower()] is None:
            raise NotImplementedError(f"Resolver not implemented for {name} ")
        return self._registry[name.lower()]
    

