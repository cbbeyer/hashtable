#!/usr/bin/env python3
from abc import ABC, abstractmethod
from binary_tree import BinaryTree

class Hashtable(ABC):
    '''Parent hashtable class'''
    @abstractmethod
    def __init__(self):
        pass
        # need to create an array of 10 objects

class StringHashtable(Hashtable):
    '''String hashtable class'''
    def __init__(self):

        pass

    def get_hash(self):
        pass

class GuidHashtable(Hashtable):
    '''String hashtable class'''
    def __init__(self):
        pass

    def get_hash(self):
        pass

class ImageHashtable(Hashtable):
    '''String hashtable class'''
    def __init__(self):
        pass

    def get_hash(self):
        pass
