## Need to implement the LRU cache: Least Recently used:
from collections import OrderedDict
import time

class LruNodeCache:
    def __init__(self, maxsize=128, ttl=60) -> None:
        self.cache = OrderedDict()
        self.maxsize = maxsize
        self.ttl = ttl

    
    def get(self, key):
        now = time.time()
        if key in self.cache:
            value, ts = self.cache.pop(key)
            if now-ts < self.ttl:
                self.cache[key] = (value, ts)
                return value
        return None
    

    def set(self, key, value):
        now = time.time()
        # Before setting call it explicitly
        self.cleanup()
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.maxsize:
            self.cache.popitem(last=False)
        self.cache[key] = (value, now)

    def cleanup(self):
        now = time.time()
        keys_to_delete = [k for k, (_, ts) in self.cache.items() if now - ts >= self.ttl]
        for k in keys_to_delete:
            del self.cache[k]




