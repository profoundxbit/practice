"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
Author: Dominique Reese
"""
import unittest
from typing import List


class TestSolution(unittest.TestCase):
    def test_one(self):
        ratings = [1, 0, 2]
        actual = candy(ratings)
        expected = 5
        self.assertEqual(expected, actual)
    def test_two(self):
        ratings = [1, 2, 2]
        actual = candy(ratings)
        expected = 4
        self.assertEqual(expected, actual)


def candy(ratings: List[int]) -> int:
    # If ratings array countains only less than 2 elements
    # return the length of the array
    if len(ratings) < 2:
        return len(ratings)

    idx = 0
    count = 1
    prev_count = 1
    runner_idx = 1
    while runner_idx <= len(ratings) - 1:
        if ratings[idx] < ratings[runner_idx]:
            prev_count += 1
            count += prev_count
        elif ratings[idx] == ratings[runner_idx]:
            prev_count = 1
            count += prev_count
        else:  # Case where ratings[idx] > ratings[runner_idx]
            desc_count = 1
            while runner_idx < len(ratings) - 1 and ratings[runner_idx] > ratings[runner_idx + 1]:
                count += desc_count
                desc_count += 1
                runner_idx += 1
            count += desc_count
            prev_count = 1
        idx = runner_idx
        runner_idx += 1
    count += 1
    return count


if __name__ == "__main__":
    unittest.main()
