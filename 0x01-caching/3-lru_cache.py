#!/usr/bin/env python3
""" Least recenly used task """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache """
    def put(self, key, item):
        """ method to store data in a cache """
        if key or item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                deleted_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(next(iter(self.cache_data)))
                print("DISCARD: {}".format(deleted_key))

    def get(self, key):
        """ method to get data in cache """
        if key is None:
            return
        return self.cache_data.get(key)
