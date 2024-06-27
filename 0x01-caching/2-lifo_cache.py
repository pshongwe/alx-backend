#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - a LIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    print("DISCARD: {}".format(self.last_key))
                    del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]


if __name__ == "__main__":
    LIFOCache = __import__('2-lifo_cache').LIFOCache

    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
