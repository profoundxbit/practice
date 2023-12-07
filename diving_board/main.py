""" **Diving Board:
    You are building a diving board by placing a bunch of planks
    of wood end-to-end. There are two types of planks, one of length shorter and one of length longer. 
    You must use exactly K planks of wood. Write a method to generate all possible lenghts for the diving board.
    
    Author: Dominique Reese
    """
import unittest


class TestSolution(unittest.TestCase):
    def test_generate_five_lengths_recursive(self):
        expected = [4, 5, 6, 7, 8]
        actual = all_lengths_recursive(4, 1, 2)

        self.assertEqual(actual, expected)

    def test_generate_five_lengths_optimal(self):
        expected = { 4, 5, 6, 7, 8 }
        actual = all_lengths_optimal(4, 1, 2)

        self.assertEqual(actual, expected)


def all_lengths_recursive(k, s, l):
    """Recursive solution. We make k decisions, each time
    choosing which plank we will put on next.  We can add completed
    plank to list (assuming we haven't seen the length before)

    Args:
        k (int): Number of planks we can use
        s (int): Value of shorter plank
        l (int): Value of longer plank
    
    Returns:
        (list): List of all possible lengths
    """

    def getAllLengths(k, total, shorter, longer, lengths):
        """Inner method which will be called recursively.

        Args:
            k (int): Number of planks we can use
            total (int): Total length of complete plank
            shorter (int): Value of shorter plank
            longer (int): Value of longer plank
            lengths (set): Set of recorded lengths
        """
        if (k == 0):
            lengths.add(total)
            return
        getAllLengths(k - 1, total + shorter, shorter, longer, lengths)
        getAllLengths(k - 1, total + longer, shorter, longer, lengths)

    lengths = set()
    getAllLengths(k, 0, s, l, lengths)
    return list(lengths)


def all_lengths_optimal(k, s, l):
    """Optimal solution. We don't actually need to go through all arrangements of planks.
    We just need to go through all unique sets of K planks (sets, not orders!).  There are only
    K + 1 ways of picking K planks if we only have two possible types:
    {0 of type A, K of type B}, {1 of type A, K-1 of type B}....

    Args:
        k (int): Number of planks we can use
        s (int): Value of shorter plank
        l (int): Value of longer plank

    Returns:
        (set): List of all possible lengths
    """
    lengths = set()
    # We know ther are only k + 1 ways of picking k planks if we only have 2 possible types.
    num_possible_lengths = k + 1
    for nShorter in range(num_possible_lengths):
        nLonger = k - nShorter
        length = nShorter * s + nLonger * l
        lengths.add(length)

    return lengths


if __name__ == "__main__":
    unittest.main()
