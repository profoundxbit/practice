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
        """We use list because list.append() takes O(1) average.
        We use dict because get() and set() take O(1) average.
        """
        self.inner = list()
        self.map = dict()

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.inner.append(val)
            last_idx = len(self.inner) - 1
            self.map[val] = last_idx #Insert val in dict for O(1) retrieval
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            idx = self.map[val] # Get index of value
            last_element = self.inner[-1] # Get last element in list
            self.inner[idx] = last_element # Replace element to be removed with last element
            self.map[last_element] = idx # Update map at last element key with new index
            self.inner.pop() # Removing last element. No longer needed as it replaced val
            self.map.pop(val) # Remove val from map
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.inner)

if __name__ == "__main__":
    unittest.main()