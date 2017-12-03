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

    # with open('strings.txt', newline='') as f:
    #     for line_i, line in enumerate(f):
    #         line = line.rstrip()
    #         value = line.lower()
    #         string_hash_table.set(line, value)
    #
    # print('String hash table:')
    # string_hash_table.debug_print()
    #
    # print()
    # print('String Lookups:')
    # print(string_hash_table.get('Indian Meal Moth'))
    # print(string_hash_table.get('Orb-Weaving Spiders (Banded Garden Spider)'))
    #
    # print()

    guid_hash_table = GuidHashtable()

    with open('guids.txt', newline='') as f:
        for line_i, line in enumerate(f):
            line = line.rstrip()
            value = line.lower()
            # guid_hash_table.set(line, value)
            guid_hash_table.set(line, line)

    guid_hash_table.debug_print()

    # guid_hash_table.get_hash('00000158691797bd77464872000a0018001b000c')
    # guid_hash_table.get_hash('00000158691797bd77464873000a0018001b000c')
    # guid_hash_table.get_hash('00000158691797bd77464874000a0018001b000c')
    # guid_hash_table.get_hash('00000158691797bd7746487c000a001800388ccf')

    # images_hash_table = ImageHashtable()
    #
    # with open('images.txt', newline='') as f:
    #     for line_i, line in enumerate(f):
    #         line = line.rstrip()
    #         value = line.lower()
    #         images_hash_table.set(line, line)
    #
    # print('Image hash table:')
    # images_hash_table.debug_print()
    #
    # print()
    # print('Image lookups:')
    # print(images_hash_table.get('document.png'))
    # print(images_hash_table.get('security_keyandlock.png'))



# Runner
if __name__ == '__main__':
    main()
    # with open('output.txt', 'w') as f:
    #     orig_stdout = sys.stdout
    #     sys.stdout = f
    #     main()
    #     sys.stdout = orig_stdout
