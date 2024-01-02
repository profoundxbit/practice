"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

URL: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
Author: Dominique Reese
"""
import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        actual = removeElement(nums, val)

        self.assertEqual(actual, len(expected_nums))
        index_to_sort = len(expected_nums)

        nums[:index_to_sort] = sorted(nums[:index_to_sort])
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)

    def test_two(self):
        nums = [3, 3]
        val = 3
        expected_nums = []
        actual = removeElement(nums, val)

        self.assertEqual(actual, len(expected_nums))
        index_to_sort = len(expected_nums)

        nums[:index_to_sort] = sorted(nums[:index_to_sort])
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)

    def test_three(self):
        nums = [1, 3]
        val = 3
        expected_nums = [1]
        actual = removeElement(nums, val)

        self.assertEqual(actual, len(expected_nums))
        index_to_sort = len(expected_nums)

        nums[:index_to_sort] = sorted(nums[:index_to_sort])
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)


def removeElement(nums: List[int], val: int) -> int:
    count, idx, swap_idx = len(nums), 0, len(nums) - 1
    while idx <= len(nums) - 1 and idx < swap_idx:
        if nums[idx] == val:
            while nums[swap_idx] == val:
                count -= 1
                swap_idx -= 1
                if swap_idx < idx:
                    return count
            nums[idx] = nums[swap_idx]
            swap_idx -= 1
            count -= 1
        idx += 1
    if len(nums) and nums[idx] == val:
        count -= 1
    return count


if __name__ == "__main__":
    unittest.main()
