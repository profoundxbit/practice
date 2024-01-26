"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

Author: Dominique Reese
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate_array(nums, k)
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(expected, nums)

    def test_two(self):
        nums = [1, 2]
        k = 1
        rotate_array(nums, k)
        expected = [2, 1]
        self.assertEqual(expected, nums)

    def test_three(self):
        nums = [1, 2, 3, 4]
        k = 2
        rotate_array(nums, k)
        expected = [3, 4, 1, 2]
        self.assertEqual(expected, nums)

    def test_four(self):
        nums = [1, 2, 3]
        k = 2
        rotate_array(nums, k)
        expected = [2, 3, 1]
        self.assertEqual(expected, nums)


def rotate_array(nums, k):
    """
        Do not return anything, modify nums in-place instead.
    """
    if k % len(nums) == 0:
        return
    idx = 0
    for _ in range(len(nums) - 1):
        swp_idx = (idx + k)
        if swp_idx > len(nums) - 1:
            swp_idx -= len(nums)

        # Perform swap
        tmp = nums[swp_idx]
        nums[swp_idx] = nums[idx]
        nums[idx] = tmp
        # If we performed swap of final index we are DONE
        if idx == len(nums) - 1:
            break
        else:  # We have more swaps to perform
            idx = swp_idx + 1


if __name__ == "__main__":
    unittest.main()
