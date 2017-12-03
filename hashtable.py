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

    def set(self, key, value):
        index = self.get_hash(key)
        self.buckets[index].set(key, value)

    def get(self, key):
        index = self.get_hash(key)
        return self.buckets[index].get(key)


    def remove(key):
        pass

    @abstractmethod
    def get_hash(key):
        pass

class StringHashtable(Hashtable):
    '''String hashtable class'''

    def get_hash(self, key):
        ascii_values = ''
        for c in key:
            if c != 's':
                temp_val = ord(c)
            else:
                temp_val = len(key)

            temp_val = temp_val * 17
            temp_val = temp_val - len(key)
            ascii_values += str(temp_val)

        ascii_values = int(ascii_values) / 3
        ascii_values * 3 * len(key)
        index = int(ascii_values) % 11 - 1

        if index < 0:
            index = 0

        return index

    def debug_print(self):
        for i in range(len(self.buckets)):
            if self.buckets[i].root is not None:
                li = self.buckets[i].walk_bfs_return(self.buckets[i].root)
                print('{}: {}'.format(i, ', '.join(li), end=''))
            else:
                print('{}: {}'.format(i, self.buckets[i].root))


class GuidHashtable(Hashtable):
    '''Guid hashtable class'''

    def get_hash(self, key):
        temp_hex = key[16:]
        temp_hex = temp_hex[:8]

        temp_hex = bin(int(temp_hex, 16))[2:]

        print(key)

        print(temp_hex)

        counter = 0
        count_hash = ''

        print('------------------')
        for c in temp_hex:

            if c == '1':
                print(c, '--')
                counter += 1
                counter = counter * 3
            else:
                counter = 3

            c = c * 3 * counter

            count_hash += str(c)




            count_hash += str(counter)

        print('------------------')
        print(count_hash)

        index = int(count_hash) % 11 - 1

        if index < 0:
            index = 0

        return index


        # for c in temp_hash:
        #     if c == 1 or c == 3 or c == 5:
        #         temp_val = int(c) * 13
        #         new_hash += str(temp_val)
        #     elif c == 0 or c == 2 or c == 4:
        #         temp_val = int(c) * 17
        #         new_hash += str(temp_val)
        #     else:
        #         temp_val = int(c) * 3
        #         new_hash += str(temp_val)

        # index = int(new_hash) % 11 - 1
        #
        # print(index)


        # returns a number 0-9

    def debug_print(self):
        for i in range(len(self.buckets)):
            if self.buckets[i].root is not None:
                li = self.buckets[i].walk_bfs_return(self.buckets[i].root)
                print('{}: {}'.format(i, ', '.join(li), end=''))
            else:
                print('{}: {}'.format(i, self.buckets[i].root))


class ImageHashtable(Hashtable):
    '''Image hashtable class'''

    def get_hash(self, key):
        with open("images/{}".format(key), "rb") as binary_file:
            f = binary_file.read()

            i = int.from_bytes(f, byteorder='big')
            index = i % 11 - 1

            if index < 0:
                index = 0

            return index

    def debug_print(self):
        for i in range(len(self.buckets)):
            if self.buckets[i].root is not None:
                li = self.buckets[i].walk_bfs_return(self.buckets[i].root)
                print('{}: {}'.format(i, ', '.join(li), end=''))
            else:
                print('{}: {}'.format(i, self.buckets[i].root))
