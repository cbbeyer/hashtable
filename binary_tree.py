#!/usr/bin/env python3
from collections import deque

class BinaryTree(object):
    '''Makes a binary tree object'''

    def __init__(self):
        '''Constructor'''
        self.root = None


    def set(self, key, value):
        node = Node(key, value)

        if self.root is None:
            self.root = node

        else:
            self._add_node(self.root, node)


    def _add_node(self, old_node, new_node):
        if new_node.key >= old_node.key:
            if old_node.right is not None:
                self._add_node(old_node.right, new_node)
            else:
                old_node.right = new_node
                new_node.parent = old_node
        else:
            if old_node.left is not None:
                self._add_node(old_node.left, new_node)
            else:
                old_node.left = new_node
                new_node.parent = old_node


    def get(self, key):
        try:
            node = self._find(key, self.root)
            print(node.value)
        except:
            print('This key could not be found in the binary tree')

    def remove(self, key):
        node = self._find(key, self.root)

        if not node.left and not node.right:
            if node.parent.key < node.key:
                node.parent.right = None
            else:
                node.parent.left = None

        elif node.left and not node.right:
            node.parent.left = node.left
            node.left.parent = node.parent
            node.parent = None

        elif node.right and not node.left:
            node.parent.right = node.right
            node.right.parent = node.parent
            node.parent = None

        else:
            replace_child = self.replace_with_child(node.left)
            node.key = replace_child.key
            node.value = replace_child.value
            remove_right = self._find(replace_child.parent.key, self.root)
            replace_child.parent = None
            remove_right.right = None


    def replace_with_child(self, node):
        if node.right is not None:
            return self.replace_with_child(node.right)
        else:
            return node

    def walk_dfs_inorder(self, node):
        if(node != None):
            self.walk_dfs_inorder(node.left)
            print('{}'.format(node.value))
            self.walk_dfs_inorder(node.right)


    def walk_dfs_preorder(self, node):
        if(node != None):
            print('{}'.format(node.value))
            self.walk_dfs_preorder(node.left)
            self.walk_dfs_preorder(node.right)


    def walk_dfs_postorder(self, node):
        if(node != None):
            self.walk_dfs_postorder(node.left)
            self.walk_dfs_postorder(node.right)
            print('{}'.format(node.value))


    def walk_bfs(self, node):
        q = deque([node])
        current_level = 1

        while len(q) > 0:

            current_node = q.popleft()
            print(current_node.value)

            if current_node.left != None:
                q.append(current_node.left)

            if current_node.right != None:
                q.append(current_node.right)

            current_level += 1

    def debug_print(self):
        current_level = [self.root]

        while current_level:
            next_level = list()

            for node in current_level:
                if node.parent is not None:
                    print('{}({}) '.format(node.key, node.parent.key), end='')
                else:
                    print('{}({}) '.format(node.key, '-'), end='')

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print()
            current_level = next_level

    def _replace_node(self, old_node, new_node):
        pass


    def _find(self, key, node):
        if node is not None:
            if node.key < key:
                return self._find(key, node.right)
            elif node.key > key:
                return self._find(key, node.left)
            elif node.key == key:
                return node
            else:
                error_message = 'This key could not be found in the binary tree.'
                return error_message

class Node(object):
    '''Creates a node on the binary tree'''

    def __init__(self, key, value, parent=None, left=None, right=None):
        '''Constructor'''
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
