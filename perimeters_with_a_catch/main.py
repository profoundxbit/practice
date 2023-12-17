"""Problem taken from: https://edabit.com/challenge/WEvqZTFcHeYzFn74c

Write a function that takes a number and returns the perimeter of either a circle or a square. The input will be in the form (letter l, number num) where the letter will be either "s" for square, or "c" for circle, and the number will be the side of the square or the radius of the circle.

Use the following formulas:

Perimeter of a square: 4 * side.
Perimeter of a circle: 6.28 * radius.
The catch is you can only use arithmetic or comparison operators, which means:

No if... else statements.
No objects.
No arrays.
No formatting methods, etc.
The goal is to write a short, branch-free piece of code.
"""

import unittest

class TestSolution(unittest.TestCase):
    def test_square_7_perimeter(self):
        actual = perimeter("s", 7)
        expected = 28
        self.assertEqual(actual, expected)
    
    def test_circle_4_perimeter(self):
        actual = perimeter("c", 4)
        expected = 25.12
        self.assertEqual(actual, expected)
        

def perimeter(letter, num):
    circle_perimeter = int(letter.lower() == "c") * (num * 6.28)
    square_perimeter = int(letter.lower() == "s") * (num * 4)
    return circle_perimeter + square_perimeter

if __name__ == "__main__":
    unittest.main()
