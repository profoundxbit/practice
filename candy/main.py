"""
There are n children standing in a line. Each child is assigned a rating value given in the integer list ratings.

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

    def test_seven(self):
        ratings = [1, 2, 87, 87, 87, 2, 1]
        actual = candy(ratings)
        expected = 13
        self.assertEqual(expected, actual)


def candy(ratings: List[int]) -> int:
    """Algorithm is to initilize list (candy list) of same length as ratings list filled with 1's.
    First iterate through ratings list ensuring elements which are greater have a higher
    candy count than their left neighbor in the candy list. Then iterate again through 
    ratings list, this time backwards ensuring elements which are greater have a higher
    candy count than their right neighbor in the candy list. Return the sum of the candy
    counts of the candy list

    Args:
        ratings (List[int]): Input ratings list

    Returns:
        int: Minumum number of candies needed to satisfy
    """
    
    # Initilize candy list filled with 1's. Same length as ratings list
    candy_list = [1] * len(ratings)
    n = len(ratings)

    # Iterate through ratings list handling increasing elements
    for i in range(1, n):
        # Increasing
        if ratings[i] > ratings[i-1]:
            candy_list[i] = candy_list[i-1] + 1

    # Iterate through ratings list backwards handling decreasing elements
    for i in reversed(range(1, n)):
        # Decreasing
        if ratings[i-1] > ratings[i] and candy_list[i-1] <= candy_list[i]:
            candy_list[i-1] = candy_list[i] + 1

    # Total up candy count to be returned
    total = sum(candy_list)
    return total


if __name__ == "__main__":
    unittest.main()
