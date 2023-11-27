import unittest

"""This module represents my work with tree data structure.

    Author: Dominique Reese
"""


class Tree:
    def __init__(self, root=None):
        self.root = root

    def sum_levels(self):
        result = []

        if self.root is not None:
            queue = []
            queue.append(self.root)
            while queue:
                lvl_sum = 0
                lvl_size = len(queue)
                for _ in range(lvl_size):
                    node = queue.pop(0)
                    lvl_sum += node.value

                    for child in node.children:
                        queue.append(child)
                result.append(lvl_sum)

        return result


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class TestTreeMethods(unittest.TestCase):
    def test_sum_levels(self):
        root = Node(1)
        child2 = Node(2)
        child3 = Node(3)
        child4 = Node(4)
        child5 = Node(5)
        child6 = Node(6)
        child7 = Node(7)

        root.add_child(child2)
        root.add_child(child3)
        root.add_child(child4)
        child2.add_child(child5)
        child2.add_child(child6)
        child3.add_child(child7)

        tree = Tree(root)

        result = tree.sum_levels()
        self.assertEqual(result, [1, 9, 18])


if __name__ == "__main__":
    unittest.main()
