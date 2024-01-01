"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

URL: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
Author: Dominique Reese
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [3, 2, 1, 3]
        val = 3
        expected_nums = [1, 2]
        actual = remove_element(nums, val)

        self.assertEqual(actual, len(expected_nums))
        index_to_sort = len(expected_nums)

        nums[:index_to_sort] = sorted(nums[:index_to_sort])
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)
    
    def test_two(self):
        nums = [3, 3]
        val = 3
        expected_nums = []
        actual = remove_element(nums, val)

        self.assertEqual(actual, len(expected_nums))
        index_to_sort = len(expected_nums)

        nums[:index_to_sort] = sorted(nums[:index_to_sort])
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)
    
    def test_three(self):
        nums = [1, 3]
        val = 3
        expected_nums = [1]
        actual = remove_element(nums, val)

        self.assertEqual(actual, len(expected_nums))
        index_to_sort = len(expected_nums)

        nums[:index_to_sort] = sorted(nums[:index_to_sort])
        for i, n in enumerate(expected_nums):
            self.assertEqual(nums[i], n)
            

def remove_element(nums, val):
    if len(nums) == 0:
        return 0
    
    idx, removed = 0, 0
    last_idx = len(nums) - 1
    
    while idx <= last_idx:
        if nums[idx] == val:
            swap_idx = idx
            while nums[swap_idx] == val:
                swap_idx += 1
                if swap_idx > last_idx:
                    if idx == 0:
                        return 0 # All elements == val
                    else:
                        return len(nums) - removed
            tmp = nums[idx]
            nums[idx] = nums[swap_idx]
            nums[swap_idx] = tmp
            removed += 1

        idx += 1
        
    return len(nums) - removed

if __name__ == "__main__":
    unittest.main()
