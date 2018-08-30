from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections
class LruCache:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity
        return

    def lookup(self, isbn):
        # TODO - you fill in here.
        if isbn in self._isbn_price_table:
            # remove and re-add to put make it most recently used
            price = self._isbn_price_table.pop(isbn)
            self._isbn_price_table[isbn] = price
        else:
            price = -1
        return price

    def insert(self, isbn, price):
        print("insert params isbn={}, price={}".format(isbn, price))
        # TODO - you fill in here.
        # if isbn is already in cache, remove and re-add so that it is last item (most recently used)
        # in cache which is an instance of OrderedDict
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            # if at capacity, remove LRU key to make room
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price
        # print("insert result isbn={}, price={}".format(isbn, self._isbn_price_table[isbn]))
        print("+insert result ", self._isbn_price_table.items())

    def erase(self, isbn):
        # TODO - you fill in here.
        if isbn in self._isbn_price_table:
            del self._isbn_price_table[isbn]
            return True
        else:
            return False


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
