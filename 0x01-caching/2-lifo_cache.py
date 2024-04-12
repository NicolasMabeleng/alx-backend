#!/usr/bin/env python3

""" A class LIFOCache that inherits from
    BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class LIFOCache inherits from subclass BaseCaching
    """
    def __init__(self):
        """ Constructor
        """
        super().__init__()

    def put(self, key, item):
        """ save key/value in cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data:
            # get the last key in the dictionary and remove [FILO]
            last_key = list(self.cache_data)[-1]
            print(f'DISCARD: {last_key}')
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """ retrieve value by key from cache
        """
        if key is None or key not in self.cache_data:
            return

        return self.cache_data[key]
