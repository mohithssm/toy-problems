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

# class lru:
#     def __init__(self, size):
#         self.size = size
#         self.cache = {}
#         self.count_lr = {}
#     def put(self, key, data):
#         if(key not in self.cache):
#             if(len(self.cache) == self.size):
#                 least = min(self.count_lr.keys(), key = lambda k:self.count_lr[k])
#                 self.cache.pop(least)
#                 self.count_lr.pop(least)
#             self.cache[key] = data
#             self.count_lr[key] = 1
#             return "done"

#     def get(self,key):
#         if key in self.cache:
#             self.count_lr[key] += 1
#             return self.cache[key]
#         else:
#             print("No such file")

#     def get_cache(self):
#         return self.cache