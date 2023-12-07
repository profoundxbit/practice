""" **Diving Board:
    You are building a diving board by placing a bunch of planks
    of wood end-to-end. There are two types of planks, one of length shorter and one of length longer. 
    You must use exactly K planks of wood. Write a method to generate all possible lenghts for the diving board.
    
    Author: Dominique Reese
    """
import unittest


class TestSolution(unittest.TestCase):
    def test_generate_five_lengths(self):
        expected = [4, 5, 6, 7, 8]
        actual = all_lengths(4, 1, 2)

        self.assertEqual(actual, expected)


def all_lengths(k, s, l):
    """Recursive solution. We make k decisions, each time
    choosing which plank we will put on next.  We can add completed
    plank to list (assuming we haven't seen the length before)

    Args:
        k (int): Number of planks we can use
        s (int): Value of shorter plank
        l (int): Value of longer plank
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


if __name__ == "__main__":
    unittest.main()
