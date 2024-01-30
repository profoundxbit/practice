"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150

Author: Dominique Reese
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        actual = maxProfit(prices)
        self.assertEqual(actual, expected)

    def test_two(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        actual = maxProfit(prices)
        self.assertEqual(actual, expected)

    def test_tree(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        actual = maxProfit(prices)
        self.assertEqual(actual, expected)


def maxProfit(prices):
    total_profit = running_profit_total = buy_ptr = 0
    for sell_ptr, sell_price in enumerate(prices[1:], 1):
        buy_price = prices[buy_ptr]
        profit = sell_price - buy_price
        if profit < running_profit_total or profit < 0:
            total_profit += running_profit_total
            running_profit_total = 0
            buy_ptr = sell_ptr
        else:
            running_profit_total = profit

    total_profit += running_profit_total
    return total_profit


if __name__ == "__main__":
    unittest.main()
