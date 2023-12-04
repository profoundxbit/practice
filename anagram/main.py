"""Determine if two strings are anagrams? 
    exp. Care == Race,  Ranked != Ankered

    Author: Dominique Reese
"""
import unittest

class TestSolution(unittest.TestCase):
    def test_are_anagrams_one(self):
        word_one = "care"
        word_two = "race"
        
        result = are_anagrams(word_one, word_two)
        self.assertTrue(result)
        
    def test_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("Astronomer", "Moon starer"))
        self.assertTrue(are_anagrams("The Morse Code!", "Here come dots"))
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertFalse(are_anagrams("python", "java"))
        self.assertFalse(are_anagrams("abc", "def"))

    def test_case_insensitivity(self):
        self.assertTrue(are_anagrams("Listen", "Silent"))
        self.assertTrue(are_anagrams("Astronomer", "Moon Starer"))
        self.assertTrue(are_anagrams("The Morse Code!", "Here Come Dots"))

    def test_with_spaces(self):
        self.assertTrue(are_anagrams("a gentleman", "elegant man"))
        self.assertTrue(are_anagrams("rail safety", "fairy tales"))
        

def are_anagrams(input_one, input_two):
    
    # Normalize input into lowercase strings containing only letters without spaces
    input_one = "".join(char.lower() for char in input_one if char.isalpha())
    input_two = "".join(char.lower() for char in input_two if char.isalpha())
    
    # Anagrams must have same length
    if len(input_one) != len(input_two):
        return False
    
    map_one = dict()
    map_two = dict()
    # Create hashmap from each input
    # Key is character, value is occurance in string
    for char in input_one:
        map_one[char] = map_one.get(char, 0) + 1
    
    for char in input_two:
        map_two[char] = map_two.get(char, 0) + 1
    
    # Validate hashmap's key & value equality
    for char, count in map_one.items():
        if map_two.get(char, 0) != count:
            return False
        
    return True

def _are_anagrams(input_one, input_two):
    # Normalize strings
    input_one = "".join(char.lower() for char in input_one if char.isalpha())
    input_two = "".join(char.lower() for char in input_two if char.isalpha())
    
    # Sort strings
    input_one = sorted(input_one)
    input_two = sorted(input_two)
    
    return input_one == input_two

if __name__ == "__main__":
    unittest.main()