"""Sort Stack
Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). 
The stack supports the following operations: push, pop, peek, and isEmpty.
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_stack_create(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        stack_expected = Stack()
        stack_expected.push(1)
        stack_expected.push(2)
        stack_expected.push(3)

        self.assertEqual(stack.pop(), stack_expected.pop())

    def test_stack_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_stac_equality(self):
        stack = Stack()
        stack.push(1)

        expected_stack = Stack()
        expected_stack.push(1)

        self.assertEqual(stack, expected_stack)

    def test_stack_peek(self):
        stack = Stack()
        stack.push(2)
        stack.push(3)
        stack.push(1)

        self.assertEqual(stack.peek(), 1)

    def test_stack_sort(self):
        stack = Stack()
        stack.push(2)
        stack.push(3)
        stack.push(1)

        expected_stack = Stack()
        expected_stack.push(3)
        expected_stack.push(2)
        expected_stack.push(1)

        sorted_stack = stack.sort()

        self.assertEqual(sorted_stack, expected_stack)
    
    def test_stack_sort_1(self):
        stack = Stack()
        stack.push(2)

        expected_stack = Stack()
        expected_stack.push(2)

        sorted_stack = stack.sort()

        self.assertEqual(sorted_stack, expected_stack)
    
    def test_stack_sort_2(self):
        stack = Stack()
        expected_stack = Stack()

        sorted_stack = stack.sort()

        self.assertEqual(sorted_stack, expected_stack)
        
    def test_stack_sort_3(self):
        stack = Stack()
        stack.push(100)
        stack.push(2)
        stack.push(132)
        stack.push(4)

        expected_stack = Stack()
        expected_stack.push(132)
        expected_stack.push(100)
        expected_stack.push(4)
        expected_stack.push(2)

        sorted_stack = stack.sort()

        self.assertEqual(sorted_stack, expected_stack)


class Stack:
    def __init__(self):
        self._inner = []

    def peek(self) -> int:
        element = None
        if not self._is_empty():
            # last_index = len(self._inner) - 1
            element = self._inner[-1]

        return element

    def push(self, data) -> bool:
        self._inner.append(data)
        return True

    def _is_empty(self) -> bool:
        return len(self._inner) == 0

    def sort(self):
        # 2 -> 3 -> 1  -->> 3 -> 2 -> 1
        tmp_stack = Stack()
        result = Stack()
        hold = None
        while not self._is_empty():
            if hold is None:
                hold = self.pop()
            next = self.peek()
            if next is not None:
                if next > hold:
                    tmp_stack.push(hold)
                    hold = None
                else:
                    tmp_stack.push(self.pop())

            if self._is_empty():
                result.push(hold)
                hold = None
                self = tmp_stack
                tmp_stack = Stack()

        return result

    def pop(self) -> int:
        if self._is_empty():
            raise Exception("Stack is empty.")
        return self._inner.pop()

    def __eq__(self, value: object) -> bool:
        return self._inner == value._inner


if __name__ == "__main__":
    unittest.main()
