"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

https://leetcode.com/problems/3sum/

Author: Dominique Reese
"""
import unittest
from typing import List


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]

        actual = threeSum(nums)

        self.assertEqual(expected, actual)


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    map = {}
    # Iterate through array getting sum of every element with every other element
    for idx, num in enumerate(nums):
        for pidx, pnum in enumerate(nums[idx+1:], idx + 1):
            pair_sum = num + pnum
            if pair_sum not in map:
                map[pair_sum] = [[idx, pidx]]
            else:
                map[pair_sum].append([idx, pidx])

    # Iterate through nums searching map of pairs for a key which
    # when added to element == 0
    for idx, num in enumerate(nums):
        if num == 0: # If element is 0 we are looking for a pair which sums to 0
            if num in map:
                finds = list(filter(lambda x: idx not in x, map[num])) # Filter pairs which include current element already
                for x in finds:
                    result.append([nums[x[0]], nums[x[1]], 0]) #Add valid pairs to result list
        elif num < 0: # Element is negative number, therefore we're searching for positive equivalent in order to sum to 0
            num = abs(num) # Turn positive
            if num in map:
                finds = list(filter(lambda x: idx not in x, map[num]))
                for x in finds:
                    result.append([nums[x[0]], nums[x[1]], -abs(num)])
        else: # Element is positive number, therefore we're searching for negative equivalant in order to sum to 0
            num = -abs(num) # Turn negative
            if num in map:
                finds = list(filter(lambda x: idx not in x, map[num]))
                for x in finds:
                    result.append([nums[x[0]], nums[x[1]], abs(num)])

    
    unique_triplets = set()
    for x in result:
        x = sorted(x)
        x = tuple(x)
        if x not in unique_triplets:
            unique_triplets.add(x)

    unique_triplets = [list(x) for x in unique_triplets]
    return unique_triplets

if __name__ == "__main__":
    unittest.main()
