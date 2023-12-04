import unittest
"""Implement Fibonacci using memoization.
    Author: Dominique Reese
"""


class TestSolution(unittest.TestCase):
    def test_fib_memo_0(self):
        actual = fib_memo(0)
        expected = [0]

        self.assertEqual(actual, expected)

    def test_fib_memo_1(self):
        actual = fib_memo(2)
        expected = [0, 1]

        self.assertEqual(actual, expected)

    def test_fib_memo_3(self):
        actual = fib_memo(8)
        expected = [0, 1, 1, 2, 3, 5, 8, 13]

        self.assertEqual(actual, expected)

    def test_fib_memo_v2_0(self):
        actual = fib_memo_v2(0)
        expected = []

        self.assertEqual(actual, expected)

    def test_fib_memo_v2_1(self):
        actual = fib_memo_v2(2)
        expected = [0, 1]

        self.assertEqual(actual, expected)

    def test_fib_memo_v2_1(self):
        actual = fib_memo_v2(3)
        expected = [0, 1, 1]

        self.assertEqual(actual, expected)

    def test_fib_memo_v2_3(self):
        actual = fib_memo_v2(8)
        expected = [0, 1, 1, 2, 3, 5, 8, 13]

        self.assertEqual(actual, expected)
    
    def test_fib_memo_v3(self):
        actual = fib_memo_v3(9)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]

        self.assertEqual(actual, expected)


def fib_memo_v2(digits):
    result = list()
    if digits == 0:
        return result

    def __fib_memo(index, fib_map):
        if index in fib_map:
            return fib_map[index]
        else:
            fib_map[index] = __fib_memo(
                index-2, fib_map) + __fib_memo(index-1, fib_map)

        if len(result) == digits:
            return

        result.append(fib_map[index])
        return fib_map[index]

    result.append(0)
    result.append(1)
    __fib_memo(digits, {0: 0, 1: 1})
    return result

def fib_memo_v3(digits):
    result = [0, 1]

    if digits <= 1:
        return result[:digits]

    fib_map = {0: 0, 1: 1}

    for index in range(2, digits):
        fib_map[index] = fib_map[index - 2] + fib_map[index - 1]
        result.append(fib_map[index])

    return result



def fib_memo(digits):
    result = list()

    if digits == 0 or digits == 1:
        return list([0])

    for i in range(digits):
        if i == 0 or i == 1:
            result.append(i)
        else:
            value = result[i-2] + result[i-1]
            result.append(value)
    return result


if __name__ == "__main__":
    unittest.main()
