import unittest
"""Implement Fibonacci using memoization.
    Author: Dominique Reese
"""
class TestSolution(unittest.TestCase):
    def test_fib_memo_0(self):
        actual = fib_memo(0)
        expected = []
        
        self.assertEqual(actual, expected)
    
    def test_fib_memo_1(self):
        actual = fib_memo(2)
        expected = [0,1]
        
        self.assertEqual(actual, expected)
        
    def test_fib_memo_3(self):
        actual = fib_memo(8)
        expected = [0,1,1,2,3,5,8,13]
        
        self.assertEqual(actual, expected)
        

def fib_memo(digits):
    result = list()
    
    if digits == 0:
        return result
    
    for i in range(digits):
        if i == 0 or i == 1:
            result.append(i)
        else:
            value = result[i-2] + result[i-1]
            result.append(value)
    return result

if __name__ == "__main__":
    unittest.main()