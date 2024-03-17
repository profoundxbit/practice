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

        self.assertTrue(_compare_triplet_lists(actual, expected))

    def test_two(self):
        nums = [0, 1, 1]
        expected = []

        actual = threeSum(nums)

        self.assertTrue(_compare_triplet_lists(actual, expected))

    def test_three(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]

        actual = threeSum(nums)

        self.assertTrue(_compare_triplet_lists(actual, expected))


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
        if num == 0:  # If element is 0 we are looking for a pair which sums to 0
            if num in map:
                # Filter pairs which include current element already
                finds = list(filter(lambda x: idx not in x, map[num]))
                for x in finds:
                    # Add valid pairs to result list
                    result.append([nums[x[0]], nums[x[1]], 0])
        elif num < 0:  # Element is negative number, therefore we're searching for positive equivalent in order to sum to 0
            num = abs(num)  # Turn positive
            if num in map:
                finds = list(filter(lambda x: idx not in x, map[num]))
                for x in finds:
                    result.append([nums[x[0]], nums[x[1]], -abs(num)])
        else:  # Element is positive number, therefore we're searching for negative equivalant in order to sum to 0
            num = -abs(num)  # Turn negative
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

def _compare_triplet_lists(list1, list2):
    """
    Compares two lists of integer triplets regardless of order within the lists or order of the lists themselves.
    Args:
        list1: The first list of integer triplets.
        list2: The second list of integer triplets.
    Returns:
        True if the lists contain the same triplets regardless of order, False otherwise.
    """
    # Sort each triplet within both lists
    list1 = sorted(sorted(triplet) for triplet in list1)
    list2 = sorted(sorted(triplet) for triplet in list2)
    # Convert the lists to sets of tuples
    set1 = set(tuple(triplet) for triplet in list1)
    set2 = set(tuple(triplet) for triplet in list2)
    # Check if the sets are equal
    return set1 == set2


if __name__ == "__main__":
    unittest.main()
