"""Oddish vs. Evenish
Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".

For example, oddishOrEvenish(121) should return "Evenish", since 1 + 2 + 1 = 4. oddishOrEvenish(41) should return "Oddish", since 4 + 1 = 5.

https://edabit.com/challenge/r6TSNwkLZ2DgsoKiH

Author: Dominique Reese
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        expected = "Oddish"
        actual = oddishOrEvenish(43)
        self.assertEqual(actual, expected)

    def test_two(self):
        expected = "Evenish"
        actual = oddishOrEvenish(2222)
        self.assertEqual(actual, expected)

    def test_three(self):
        expected = "Oddish"
        actual = oddishOrEvenish(1)
        self.assertEqual(actual, expected)


def oddishOrEvenish(num):
    """Checks if a number is evenish (sum of digits is even) or oddish."""
    return "Evenish" if sum(int(digit) for digit in str(num)) % 2 == 0 else "Oddish"


if __name__ == "__main__":
    unittest.main()
