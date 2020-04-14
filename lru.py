class lru:
    def _init_(self, size):
        self.size = size
        self.Data = []
        self.cache = {}
    
