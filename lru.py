class lru:
    def _init_(self, size):
        self.size = size
        self.Data = []
        self.cache = {}
    
    def put(self, key):
        print("PASS put method")
    def get(self, key, default = None):
        print("PASS get method")
    def get_cache(self):
        print("PASS get_cache method")