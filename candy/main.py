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

    def test_three(self):
        ratings = [1, 1, 1]
        actual = candy(ratings)
        expected = 3
        self.assertEqual(expected, actual)

    def test_four(self):
        ratings = [1]
        actual = candy(ratings)
        expected = 1
        self.assertEqual(expected, actual)

    def test_five(self):
        ratings = []
        actual = candy(ratings)
        expected = 0
        self.assertEqual(expected, actual)

    def test_six(self):
        ratings = [1, 3, 2, 2, 1]
        actual = candy(ratings)
        expected = 7
        self.assertEqual(expected, actual)


def candy(ratings: List[int]) -> int:
    # If ratings array contains less than 2 elements
    # return the length of the array
    if len(ratings) < 2:
        return len(ratings)

    candy_list = [1] * len(ratings)
    idx = 0
    runner_idx = 1
    while runner_idx <= len(ratings) - 1:
        if ratings[idx] < ratings[runner_idx]:
            candy_list[runner_idx] = candy_list[idx] + 1
            idx = runner_idx
            runner_idx += 1
        elif ratings[idx] == ratings[runner_idx]:
            candy_list[runner_idx] = 1
            idx = runner_idx
            runner_idx += 1
        else:
            x = idx
            while runner_idx <= len(ratings) - 1 and ratings[runner_idx] < ratings[x]:
                for i in range(idx, runner_idx):
                    candy_list[i] += 1
                x = runner_idx
                runner_idx += 1
            idx = x

    total = sum(candy_list)
    return total


if __name__ == "__main__":
    unittest.main()
