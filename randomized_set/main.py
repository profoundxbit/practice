"""Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
Author: Dominique Reese
"""
import unittest
import random
class TestSolution(unittest.TestCase):
    def test_one(self):
        obj = RandomizedSet()
        param_1 = obj.insert(2)
        param_2 = obj.remove(5)
        param_3 = obj.getRandom()
        print(param_3)
        
class RandomizedSet:
    def __init__(self):
        self.inner = list()

    def insert(self, val: int) -> bool:
        if val in self.inner:
            return False
        else:
            self.inner.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.inner:
            return False
        else:
            self.inner.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.inner)

if __name__ == "__main__":
    unittest.main()