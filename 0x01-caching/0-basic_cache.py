#!/usr/bin/env python3

""" A class BasicCache that inherits from
    BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class BasicCache inherits from subclass BaseCaching
    """

    def put(self, key, item):
        """ save key/value in cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ retrieve value by key from cache
        """
        if key is None or key not in self.cache_data:
            return

        return self.cache_data[key]
