"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Author: Dominique Reese

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

"""
from typing import List
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        coins = [1, 2, 5]
        amount = 11
        actual = coinChange(coins, amount)
        expected = 3
        self.assertEqual(actual, expected)

    def test_two(self):
        coins = [2]
        amount = 3
        expected = -1
        actual = coinChange(coins, amount)
        self.assertEqual(actual, expected)

    def test_three(self):
        coins = [1]
        amount = 0
        expected = 0
        actual = coinChange(coins, amount)
        self.assertEqual(actual, expected)

    def test_four(self):
        coins = [186, 419, 83, 408]
        amount = 6249
        expected = 20
        actual = coinChange(coins, amount)
        self.assertEqual(actual, expected)


def coinChange(coins: List[int], amount: int) -> int:
    """First we sort list in descending order.  Iterate through list finding
    the first integer that is less than or equal to amount. If we've reached the end of list and amount
    is not 0 then we know the amount of money cannot be made up by any combination of the coins.
    Divide the amount by the current found integer. Add the quotient to the result. Get the remainder.
    If remainder is 0 return result. Repeat

    Args:
        coins (List[int]): List of coins of diff denominations
        amount (int): Target totoal amount of money.

    Returns:
        int: The fewest number of coins that you need to make up the amount
    """

    if amount == 0:
        return 0

    # Sort list in reverse order
    coins.sort(reverse=True)

    idx = result = 0
    list_len = len(coins)
    while idx < list_len and amount > 0:
        if coins[idx] <= amount:
            # Get the quotient and the remainder
            coin = coins[idx]
            result += amount // coin
            amount = amount % coin

        idx += 1

    if amount > 0:
        return -1
    else:
        return result


if __name__ == "__main__":
    unittest.main()
