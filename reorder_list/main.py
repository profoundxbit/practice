
import unittest


class NodeTest(unittest.TestCase):
    def test_node_creation(self):
        new_node = Node(1)
        self.assertEqual(new_node.data, 1)
        self.assertNotEqual(new_node.data, None)

    def test_node_equality(self):
        node_one = Node(1)
        node_two = Node(2)

        self.assertNotEqual(node_one, node_two)

        node_two.data = 1
        self.assertEqual(node_one, node_two)

        node_one = None
        self.assertNotEqual(node_one, node_two)

        node_one = None
        node_two = None
        self.assertEqual(node_one, node_two)


class LinkedListTest(unittest.TestCase):

    def test_list_equality(self):
        node_one = Node(1)
        node_two = Node(2)
        node_three = Node(3)

        node_one.next = node_two
        node_two.next = node_three

        expected_linked_list = LinkedList(node_one)
        actual_linked_list = LinkedList(node_one)

        self.assertEqual(expected_linked_list, actual_linked_list)

    def test_creation(self):
        """Test that a new linked list can be created with the correct head node."""
        expected_head_node = Node(1)
        expected_linked_list = LinkedList(expected_head_node)

        actual_head_node = Node(1)
        actual_linked_list = LinkedList(actual_head_node)

        self.assertEqual(expected_linked_list.head.data,
                         actual_linked_list.head.data)

    def test_reorder(self):
        """Test that a link list can be reordered as expected."""
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        one.next = four
        four.next = two
        two.next = three
        expected_linked_list = LinkedList(one)

        actual_one = Node(1)
        actual_two = Node(2)
        actual_three = Node(3)
        actual_four = Node(4)
        actual_one.next = actual_two
        actual_two.next = actual_three
        actual_three.next = actual_four
        actual_linked_list = LinkedList(actual_one)

        actual_linked_list.reorder()

        self.assertEqual(expected_linked_list, actual_linked_list)

    def test_get_length(self):
        node_one = Node(1)
        node_two = Node(2)
        node_three = Node(3)
        node_four = Node(4)

        node_one.next = node_two
        node_two.next = node_three
        node_three.next = node_four

        linked_list = LinkedList(node_one)
        self.assertEqual(linked_list.length(), 4)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        else:
            return self.data == other.data


class LinkedList:
    def __init__(self, head_node):
        self.head = head_node

    def __str__(self):
        return self.print()

    def length(self):
        length = 0
        if self and self.head:
            node = self.head
            while node:
                length += 1
                node = node.next
        return length

    def print(self):
        """Returns a string representation of the linked list."""
        node = self.head
        output = ""
        while node:
            output += f"{node.data} -> " if node.next else f"{node.data}"
            node = node.next
        return output

    def __eq__(self, other):
        node = self.head
        other_node = other.head

        while node and other_node:
            if node != other_node:
                return False

            node = node.next
            other_node = other_node.next

        if node or other_node:
            return False

        return True

    def reorder(self):
        """Reorders the linked list"""
        head = self.head

        # Find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Break list
        second = slow.next
        slow.next = None

        # Reverse second list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Prev will be head of reversed second list
        second = prev

        # Merge list
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

if __name__ == "__main__":
    unittest.main()
