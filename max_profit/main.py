"""Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

Author: Dominique Reese
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        actual = maxProfit(prices)
        self.assertEqual(actual, expected)

    def test_two(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        actual = maxProfit(prices)
        self.assertEqual(actual, expected)


def maxProfit(prices):
    result = day_one_idx = 0
    for day_two_idx, day_two_price in enumerate(prices[1:], 1):
        day_one_price = prices[day_one_idx]
        profit = day_two_price - day_one_price
        if profit < 0:
            day_one_idx = day_two_idx
        else:
            result = max(result, profit)
    return result


if __name__ == "__main__":
    unittest.main()
