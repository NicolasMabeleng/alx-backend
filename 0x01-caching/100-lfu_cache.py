#!/usr/bin/env python3

""" Create a class LFUCache that inherits from
    BaseCaching and is a caching system:
"""

from base_caching import BaseCaching
from threading import RLock


class LFUCache(BaseCaching):
    """
    An implementation of LFUCache (Least Frequently Used)
    Attributes:
        usedCnt (dict): A dictionary of cache keys for access count
        rlock (RLock): Lock accessed resources to prevent race conditions
    """

    def __init__(self):
        """Instantiation method, sets instance attributes"""
        super().__init__()
        # Dictionary to track access count for each key
        self.usedCnt = {}
        # Lock to ensure thread safety when accessing shared resources
        self.rlock = RLock()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            # Call _balance to handle eviction if necessary
            key_out = self._balance(key)
            with self.rlock:
                self.cache_data.update({key: item})
            if key_out is not None:
                print('DISCARD: {}'.format(key_out))

    def get(self, key):
        """ Get an item by key
        """
        with self.rlock:
            value = self.cache_data.get(key, None)
            if key in self.usedCnt:
                # Update access count for the key
                self.usedCnt[key] += 1
        return value

    def _balance(self, key_in):
        """ Remove the earliest item from the cache
            if it exceeds the maximum size
        """
        key_out = None
        with self.rlock:
            if key_in not in self.usedCnt:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    # Evict the least frequently used item
                    key_out = min(self.usedCnt, key=self.usedCnt.get)
                    self.cache_data.pop(key_out)
                    self.usedCnt.pop(key_out)
            # Update access count for the key
            self.usedCnt[key_in] = self.usedCnt.get(key_in, 0) + 1
        return key_out

    def upgrade_method(self, key, new_item):
        """ An upgraded version of the 'put' method that allows
            updating an existing item without changing the access count.
        """
        if key is not None and new_item is not None:
            with self.rlock:
                # Update the cache with the new item
                #  without changing the access count
                self.cache_data.update({key: new_item})
                # No need to check for eviction in this case

    def upgrade_get_method(self, key):
        """ An upgraded version of the 'get' method that returns
            both the value and the access count.
        """
        with self.rlock:
            value = self.cache_data.get(key, None)
            # Return access count (default to 0 if key not found)
            access_count = self.usedCnt.get(key, 0)
        return value, access_count
