#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - a LFU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.freq = defaultdict(int)
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]

    def evict(self):
        """ Evict the least frequently used item from the cache
        """
        min_freq = min(self.freq.values())
        lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
        if len(lfu_keys) > 1:
            for k in self.order:
                if k in lfu_keys:
                    del self.cache_data[k]
                    del self.freq[k]
                    self.order.pop(k)
                    print("DISCARD: {}".format(k))
                    break
        else:
            lfu_key = lfu_keys[0]
            del self.cache_data[lfu_key]
            del self.freq[lfu_key]
            self.order.pop(lfu_key)
            print("DISCARD: {}".format(lfu_key))


if __name__ == "__main__":
    LFUCache = __import__('100-lfu_cache').LFUCache

    my_cache = LFUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
