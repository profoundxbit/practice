"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Author: Dominique Reese
"""
import unittest


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        merge(nums1, m, nums2, n)

        expected = [1, 2, 2, 3, 5, 6]
        self.assertEqual(nums1, expected)

    def test_two(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0

        merge(nums1, m, nums2, n)

        expected = [1]
        self.assertEqual(nums1, expected)

    def test_three(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1

        merge(nums1, m, nums2, n)

        expected = [1]
        self.assertEqual(nums1, expected)

    def test_four(self):
        nums1 = [99, 999, 9999, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3

        merge(nums1, m, nums2, n)

        expected = [1, 2, 3, 99, 999, 9999]
        self.assertEqual(nums1, expected)


def merge(nums1, m, nums2, n):

    nums1_idx = m - 1
    nums2_idx = n - 1
    idx = (m + n) - 1

    while nums2_idx >= 0 and nums1_idx >= 0:
        if nums2[nums2_idx] >= nums1[nums1_idx]:
            nums1[idx] = nums2[nums2_idx]
            nums2_idx = nums2_idx - 1
        else:
            nums1[idx] = nums1[nums1_idx]
            nums1[nums1_idx] = 0
            nums1_idx = nums1_idx - 1
        idx = idx - 1

    while nums2_idx >= 0:
        nums1[nums2_idx] = nums2[nums2_idx]
        nums2_idx = nums2_idx - 1


if __name__ == "__main__":
    unittest.main()
