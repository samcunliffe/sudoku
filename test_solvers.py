
import unittest
import numpy
from sudoku import Sudoku
from solvers import solve_computerphile
from data import examples


class TestSolvers(unittest.TestCase):


    def _test_computerphile(self, arr):
        """Test the computerphile algorithm for one puzzle"""
        s = Sudoku(arr)
        print(s)
        solve_computerphile(s)
        print('')

    def test_computerphile(self):
        """Test the computerphile algorithm against all examples in data"""
        for example in examples:
            self._test_computerphile(example)


if __name__ == "__main__":
    unittest.main()

