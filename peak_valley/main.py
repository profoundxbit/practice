"""Peaks and Valleys
In an array of integers, a "peak" is an element which is greater than or equal to the adjacent integers and a "valley" 
is an element which is less than or equal to the adjacent integers. 
For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys.  
Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

Author: Dominique Reese
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_simple_peak_valley(self):
        input = [5, 3, 1, 2, 3]
        actual = sort_peaks_and_valleys(input)
        expected = [5, 1, 3, 2, 3]
        self.assertEqual(actual, expected)

    def test_sort_peaks_and_valleys_example(self):
        arr = [5, 8, 6, 2, 3, 4, 6]
        expected_result = [8, 5, 6, 2, 6, 3, 4]
        sort_peaks_and_valleys(arr)
        self.assertEqual(arr, expected_result)

    def test_sort_peaks_and_valleys_empty_array(self):
        arr = []
        expected_result = []
        sort_peaks_and_valleys(arr)
        self.assertEqual(arr, expected_result)

    def test_sort_peaks_and_valleys_single_element(self):
        arr = [7]
        expected_result = [7]
        sort_peaks_and_valleys(arr)
        self.assertEqual(arr, expected_result)

    def test_sort_peaks_and_valleys_all_equal_elements(self):
        arr = [5, 5, 5, 5, 5]
        expected_result = [5, 5, 5, 5, 5]
        sort_peaks_and_valleys(arr)
        self.assertEqual(arr, expected_result)

    def test_sort_peaks_and_valleys_alternating_elements(self):
        arr = [1, 3, 2, 5, 4, 7, 6]
        expected_result = [3, 1, 5, 2, 7, 4, 6]
        sort_peaks_and_valleys(arr)
        self.assertEqual(arr, expected_result)

    def test_sort_peaks_and_valleys_repeated_elements(self):
        arr = [1, 3, 2, 3, 5, 4, 7, 6, 7]
        expected_result = [3, 1, 3, 5, 2, 7, 4, 7, 6]
        sort_peaks_and_valleys(arr)
        self.assertEqual(arr, expected_result)


def sort_peaks_and_valleys(input):
    peak_or_valley_flag = 1  # Peak == 1  Valley == 0
    curr_idx = 0
    # Iterate until last element. Last element can be ignored
    while curr_idx < (len(input) - 1):
        swap_idx = curr_idx
        for i, element in enumerate(input[curr_idx:]):
            if peak_or_valley_flag == 1:  # Peak case
                if element > input[swap_idx]:
                    # Need to add current index to get proper index into input array
                    swap_idx = (i + curr_idx)
            else:  # Valley case
                if element < input[swap_idx]:
                    swap_idx = (i + curr_idx)
        # Perform swap
        temp = input[curr_idx]
        input[curr_idx] = input[swap_idx]
        input[swap_idx] = temp

        curr_idx += 1  # Move to next element

        peak_or_valley_flag = 0 if peak_or_valley_flag == 1 else 1  # Flip flag

    return input


if __name__ == "__main__":
    unittest.main()
