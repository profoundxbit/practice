"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

https://leetcode.com/problems/intersection-of-two-arrays/

Author: Dominique Reese
"""
from typing import List
import unittest
class TestSolution(unittest.TestCase):
    def test_one(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        actual = intersection(nums1, nums2)
        expected = [2]
        self.assertEqual(expected, actual)
    
    def test_two(self):
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        actual = intersection(nums1, nums2)
        expected = [9, 4]
        self.assertEqual(expected, actual)


def intersection(nums1: List[int], nums2: List[int]):
    """In order to return the intersection with unique elements between two input arrays
    we can use a hash-set.  Create a hash-set from the first input array. Iterate through the
    second input array. Once an element has been found the to be present in the hash-set add it
    to the result array; be sure to then remove it from the hash-set for proper
    duplicate handling.

    Args:
        nums1 (List[int]): Input array
        nums2 (List[int]): Second Input array
    """
    base_set = set(nums1)
    result = list()
    
    for num in nums2:
        if num in base_set:
            result.append(num)
            base_set.remove(num) #Element found in set, remove from set. Any duplicates found after will be removed.
            
    return result # result contains unique intersection
    
    
if __name__ == "__main__":
    unittest.main()