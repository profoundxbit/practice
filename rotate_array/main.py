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
    
    def test_five(self):
        nums = [1, 2]
        k = 3
        rotate_array(nums, k)
        expected = [2, 1]
        self.assertEqual(expected, nums)


def rotate_array(nums, k):
    """
        Do not return anything, modify nums in-place instead.
    """
    if k % len(nums) == 0:
        return
    nums_len = len(nums)
    queue_len = k if k < nums_len else nums_len
    nums_queue = [(i, nums[i]) for i in range(queue_len)]
    while nums_queue:
        curr = nums_queue.pop(0)
        idx_to_replace = curr[0] + k
        
        if idx_to_replace >= nums_len:
            idx_to_replace %= nums_len
        else:
            nums_queue.append((idx_to_replace, nums[idx_to_replace]))
        
        nums[idx_to_replace] = curr[1]

if __name__ == "__main__":
    unittest.main()
