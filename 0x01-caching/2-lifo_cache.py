#!/usr/bin/env python3
""" Last in first out tasks """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache """
    def put(self, key, item):
        """ method to store data in cache """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                deleted_key = list(self.cache_data.keys())[-1]
                self.cache_data.popitem()
                print("DISCARD: {}".format(deleted_key))
            self.cache_data[key] = item

    def get(self, key):
        """ method to get data in cache """
        if key is None:
            return
        return self.cache_data.get(key)
