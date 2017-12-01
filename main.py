#!/usr/bin/env python3
import sys

from binary_tree import BinaryTree
from hashtable import Hashtable, StringHashtable, GuidHashtable, ImageHashtable


def main():
    '''Main program'''

    test_hash = StringHashtable()


# Runner
if __name__ == '__main__':
    main()
    # with open('output.txt', 'w') as f:
    #     orig_stdout = sys.stdout
    #     sys.stdout = f
    #     main()
    #     sys.stdout = orig_stdout
