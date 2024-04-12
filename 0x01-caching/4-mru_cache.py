#!/usr/bin/env python3

""" A class MRUCache that inherits from
    BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class MRUCache
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()
        self.used = []

    def put(self, key, item):
        """ save key/value in cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.used.remove(key)
        elif len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            # get the Most Recently Used key and remove it [MRU]
            unUsed_key = self.used.pop(-1)
            while unUsed_key in self.used:
                self.used.remove(unUsed_key)

            print(f'DISCARD: {unUsed_key}')
            del self.cache_data[unUsed_key]

        self.cache_data[key] = item
        self.used.append(key)

    def get(self, key):
        """ retrieve value by key from cache
        """
        if key is None or key not in self.cache_data:
            return

        self.used.remove(key)
        self.used.append(key)
        return self.cache_data[key]
