"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

Author: Dominique Reese
"""
from typing import List
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        actual = hIndex(citations)
        self.assertEqual(expected, actual)

    def test_two(self):
        citations = [1, 3, 1]
        expected = 1
        actual = hIndex(citations)
        self.assertEqual(expected, actual)

    def test_three(self):
        citations = [1]
        expected = 1
        actual = hIndex(citations)
        self.assertEqual(expected, actual)


def hIndex(citations: List[int]) -> int:
    """Sort list in descending order.
    Iterate through sorted list increasing count
    of h-index while current list element is
    greater than h-index.

    Args:
        citations (List[int]): integer array

    Returns:
        int: int representing the calculated h-index 
    """
    idx = h_index = 0
    citations.sort(reverse=True)
    while idx <= len(citations) - 1 and citations[idx] > h_index:
        idx += 1
        h_index += 1
    return h_index


if __name__ == "__main__":
    unittest.main()
