"""
Reverse the Case
Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.

Author: Dominique Reese
"""
import unittest

class TestSolution(unittest.TestCase):
    def test_one(self):
        input = "HeLLo WORld"
        expected = "hEllO worLD"
        
        actual = reverse_case(input)
        self.assertEqual(actual, expected)
        
    def test_two(self):
        input = "DOMINIQUE reese"
        expected = "dominique REESE"
        
        actual = reverse_case(input)
        self.assertEqual(actual, expected)
    
    def test_three(self):
        input = "E"
        expected = "e"
        
        actual = reverse_case(input)
        self.assertEqual(actual, expected)
    
    def test_four(self):
        input = ""
        expected = ""
        
        actual = reverse_case(input)
        self.assertEqual(actual, expected)
    
    def test_five(self):
        input = "/?.!A"
        expected = "/?.!a"
        
        actual = reverse_case(input)
        self.assertEqual(actual, expected)

def reverse_case(input):
    result = ""
    
    def is_uppercase_letter(ascii_code):
        return True if (ascii_code >= 65 and ascii_code <= 90) else False
    
    def is_lowercase_letter(ascii_code):
        return True if (ascii_code >= 97 and ascii_code <= 122) else False
    
    def is_letter(ascii_code):
        return True if is_uppercase_letter(ascii_code) or  is_lowercase_letter(ascii_code) else False
    
    for ch in input:
        ascii_code = ord(ch)
        if is_letter(ascii_code):
            letter = (ascii_code + 32) if is_uppercase_letter(ascii_code) else (ascii_code - 32)
            result += chr(letter)
        else:
            result += ch
    
    return result
if __name__ == "__main__":
    unittest.main()