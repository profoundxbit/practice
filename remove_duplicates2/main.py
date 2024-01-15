"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

Author: Dominique Reese
"""
import unittest
from typing import List


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [1, 1, 1, 2, 2, 3]
        expected_nums = [1, 1, 2, 2, 3]

        k = removeDuplicates(nums)

        self.assertEqual(k, len(expected_nums))

        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)

    def test_two(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected_nums = [0, 0, 1, 1, 2, 3, 3]

        k = removeDuplicates(nums)

        self.assertEqual(k, len(expected_nums))

        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)


def removeDuplicates(nums: List[int]) -> int:
    idx = 0
    p = 1
    while p <= len(nums) - 1:
        if nums[p] == nums[idx]:  # Duplicate Found
            idx += 1
            nums[idx] = nums[p]  # Set next element to found duplicate
            while p <= len(nums) - 1 and nums[p] == nums[idx]:
                p += 1  # Skip all other duplicate elements, we have found 2

        # If we found next unique element
        if p <= len(nums) - 1 and nums[p] != nums[idx]:
            idx += 1
            nums[idx] = nums[p]

        p += 1
    return idx + 1


if __name__ == "__main__":
    unittest.main()
