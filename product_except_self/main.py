"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Author: Dominique Reese
"""
from typing import List
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        actual = product_except_self(nums)
        self.assertEqual(actual, expected)

    def test_two(self):
        nums = [1, 0]
        expected = [0, 1]
        actual = product_except_self(nums)
        self.assertEqual(actual, expected)

    def test_three(self):
        nums = [0, 1]
        expected = [1, 0]
        actual = product_except_self(nums)
        self.assertEqual(actual, expected)

    def test_four(self):
        nums = [1, 1, 1]
        expected = [1, 1, 1]
        actual = product_except_self(nums)
        self.assertEqual(actual, expected)

    def test_five(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        actual = product_except_self(nums)
        self.assertEqual(actual, expected)


def product_except_self(nums: List[int]) -> List[int]:
    """Initilize result list of same length as nums list with None.
    Iterate nums list multiplying all elements
    of result list which are not at same position/index
    as current nums list iteration element. If index of
    result list holds None just insert element of nums.


    Args:
        nums (List[int]): Input list

    Returns:
        List[int]: Result list where result[i] is equal to the product of all the elements of nums except nums[i]. 
    """

    def update_list(lst: List[int], lst_idx: int, value: int):
        """Inner method to update provided index of provided list
        accordingly.  If provided index of list holds value of None
        simply insert provided value at index. If provided index of list
        holds value other than None then set provided index value equal
        to result of multiplying provided index's current value with provided
        input value.

        Args:
            lst (List[int]): Input list
            lst_idx (int): Index of list where value is to be updated
            value (int): Input value
        """
        if lst[lst_idx] == None:
            lst[lst_idx] = value
        else:
            lst[lst_idx] *= value

    # Creating result array of same length of nums pre-populated with None
    result = [None] * len(nums)

    for idx, element in enumerate(nums):
        for res_idx in range(len(result)):
            if idx == res_idx:  # Skip updating index of result array when processing element of nums list at same index
                continue
            else:
                # Update specific result list index
                update_list(result, res_idx, element)

    return result


if __name__ == "__main__":
    unittest.main()
