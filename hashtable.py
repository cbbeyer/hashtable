#!/usr/bin/env python3
from abc import ABC, abstractmethod
from binary_tree import BinaryTree

class Hashtable(ABC):
    '''Parent hashtable class'''

    def __init__(self):
        self.buckets = []

        for i in range(10):
            new_binary_tree = BinaryTree()
            self.buckets.append(new_binary_tree)

    def set(self, key, value, index):
        # print('{}...{}, {}'.format(index, key, value))
        self.buckets[index].set(key, value)

    def get(key):
        pass

    def remove(key):
        pass

    @abstractmethod
    def get_hash(key):
        pass

class StringHashtable(Hashtable):
    '''String hashtable class'''

    # pass value as well?
    def get_hash(self, key):
        ascii_values = ''
        for c in key:
            if c != 's':
                temp_val = ord(c)
            else:
                temp_val = len(key)

            temp_val = temp_val * 17
            ascii_values += str(temp_val)

        ascii_values = int(ascii_values) / 3
        index = int(ascii_values) % 9

        # PASS VALUE AS PARAMETER?
        value = key.lower()

        self.set(key, value, index)


        # call set in this method
        # store to array
        # returns a number 0-9

    def debug_print(self):
        for i in range(len(self.buckets)):
            if self.buckets[i].root is not None:
                li = self.buckets[i].walk_bfs_return(self.buckets[i].root)
                print('{}: {}'.format(i, ', '.join(li), end=''))
            else:
                print('{}: {}'.format(i, self.buckets[i].root))


class GuidHashtable(Hashtable):
    '''String hashtable class'''

    def get_hash(self, key):
        pass


        # returns a number 0-9

    def debug_print(self):
        pass


class ImageHashtable(Hashtable):
    '''String hashtable class'''

    def get_hash(self, key):
        pass


        # returns a number 0-9

    def debug_print(self):
        pass
