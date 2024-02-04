"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

Author: Dominique Reese
"""
from typing import List
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [3, 2, 1, 0, 4]
        expected = False
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_two(self):
        nums = [2, 3, 1, 1, 4]
        expected = True
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_three(self):
        nums = [1, 0]
        expected = True
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_four(self):
        nums = [0, 0, 5]
        expected = False
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_five(self):
        nums = [0, 1]
        expected = False
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_six(self):
        nums = [1, 1, 1]
        expected = True
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_seven(self):
        nums = [3, 0, 0, 0]
        expected = True
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_eight(self):
        nums = [0]
        expected = False
        actual = canJump(nums)
        self.assertEqual(expected, actual)

    def test_eight(self):
        nums = [0, 2, 3]
        expected = False
        actual = canJump(nums)
        self.assertEqual(expected, actual)


def canJump(nums):
    """Searching in reverse from the last index
    find the first position where jumping 
    from reaches the current index. If no suitable position
    is found then the last index cannot be reached. If a
    position is found set the index of postion as the current index.
    Repeat until current index is the index of the start of the list; 0.

    Args:
        nums (List[int]): integer array

    Returns:
        bool: Boolean indicating if last index can be reached 
    """
    idx = len(nums) - 1
    for position in range(idx - 1, -1, -1):
        maxJumpIndex = position + nums[position]
        if maxJumpIndex >= idx:
            idx = position

    return True if idx == 0 else False


if __name__ == "__main__":
    unittest.main()
