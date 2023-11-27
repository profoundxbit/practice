"""
tree_practice.py

This module represents my work in understanding binary search trees.

Author: Dominique Reese
"""


class BinaryTree:
    def __init__(self):
        self._root = None

    def insert(self, data):
        """Inserts a new node in the tree

        Args:
            data (int): The integer housed as the node's data
        """
        node = self.__Node(data)
        if self._root is None:
            self._root = node
            return

        current, parent = self._root, None
        while current:
            parent, current = current, current.left if data < current.data else current.right

        if data < parent.data:
            parent.left = node
        else:
            parent.right = node

    def traverse(self, traversal_type = "in", action=print):
        if traversal_type not in ["in", "pre", "post"]:
            raise ValueError("traversal_type must be any of ['in', 'pre', 'post']")
 
        stack = []
        current = self._root
        if traversal_type == "in":
            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left

                current = stack.pop()
                action(current.data)
                
                current = current.right                            
                            
    def sum_levels(self):
        result = []
        if self._root is None:
            return result
        queue = [self._root]
        while queue:
            lvl_len = len(queue)
            lvl_sum = 0
            for _ in range(lvl_len):
                node = queue.pop(0)
                lvl_sum += node.data
                if node.left:
                    queue.append(node.left)
            
                if node.right: 
                    queue.append(node.right)
            result.append(lvl_sum)
        return result
            
            
    class __Node:
        """
        Class representing a binary tree node.
        """

        def __init__(self, data: int = None):
            self.data = data
            self.right = None
            self.left = None


def main():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(20)
    tree.insert(1)
    tree.insert(12)
    tree.insert(25)
  
    tree.traverse()
    sum_levels_result = tree.sum_levels()
    print(sum_levels_result)

if __name__ == "__main__":
    main()
