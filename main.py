#!/usr/bin/env python3
import sys

from binary_tree import BinaryTree
from hashtable import Hashtable, StringHashtable, GuidHashtable, ImageHashtable


def main():
    '''Main program'''

    string_hash_table = StringHashtable()

    # string_hash_table.get_hash('Aphids')
    # string_hash_table.get_hash('Carpet/Warehouse Beetles')
    # string_hash_table.get_hash('Armyworms/Cutworms')
    # string_hash_table.get_hash('Longhorned/Roundheaded Wood Borers')
    # string_hash_table.get_hash('Weevils/Bark Beetles')
    # string_hash_table.get_hash('Ants')
    #
    # string_hash_table.debug_print()

    with open('strings.txt', newline='') as f:
        for line_i, line in enumerate(f):
            line = line.rstrip()
            value = line.lower()
            string_hash_table.set(line, value)

    string_hash_table.debug_print()

    # Should we be looking up on the key? or the value?
    print()
    print(string_hash_table.get('Indian Meal Moth'))
    print(string_hash_table.get('Orb-Weaving Spiders (Banded Garden Spider)'))

    print()

# Runner
if __name__ == '__main__':
    main()
    # with open('output.txt', 'w') as f:
    #     orig_stdout = sys.stdout
    #     sys.stdout = f
    #     main()
    #     sys.stdout = orig_stdout
