"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
Author: Dominique Reese
"""
import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [2, 2, 3, 3]
        expected_nums = [2, 3]
        actual = removeDuplicates(nums)

        self.assertEqual(actual, len(expected_nums))
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)
    
    def test_two(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_nums = [0, 1, 2, 3, 4]
        actual = removeDuplicates(nums)

        self.assertEqual(actual, len(expected_nums))
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)


    
    
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    p = idx = 0
    while p <= len(nums) - 1:
        if nums[p] != nums[idx]: # Unique element found
            idx += 1 # Increment index for assignment
            nums[idx] = nums[p] # Assign unique element to index
        p += 1
        
    return idx + 1 # Index + 1 equals the number of unique elements

if __name__ == "__main__":
    unittest.main()