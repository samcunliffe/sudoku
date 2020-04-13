
import unittest
import numpy
from sudoku import Sudoku

solveable_list = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solveable_array = numpy.array(solveable_list)


class TestSudokuMethods(unittest.TestCase):
    """Test methods for my wrapper class"""

    def test_list_constructor(self):
        """Test that a vanilla python list construction works"""
        self.assertIsInstance(Sudoku(solveable_list), Sudoku)

    def test_array_constructor(self):
        """Test that a numpy.array construction works"""
        self.assertIsInstance(Sudoku(solveable_array), Sudoku)

    def test_constructor_fail(self):
        """Test TypeErrors are raised for garbage in"""
        with self.assertRaises(TypeError):
            Sudoku("nonsense")
        with self.assertRaises(TypeError):
            Sudoku(1)
        with self.assertRaises(TypeError):
            Sudoku(solveable_list[-1])

    def test_print(self):
        """Test that I can print the thing"""
        print(Sudoku(solveable_list))

    def test_row(self):
        """Test that the row method returns the correct thing"""
        self.assertListEqual(
            list(Sudoku(solveable_list).row(7)),
            [0, 0, 0, 4, 1, 9, 0, 0, 5])

    def test_column(self):
        """Test that the column method returns the correct thing"""
        self.assertListEqual(
            list(Sudoku(solveable_list).column(7)),
            [0, 0, 6, 0, 0, 0, 8, 0, 7])

    def test_cell(self):
        """Test that the cell method returns the correct thing"""
        a = [[0, 6, 0],
             [8, 0, 3],
             [0, 2, 0]]
        b = Sudoku(solveable_list).cell(4)
        print(a)
        print(b)
        for j, row in enumerate(a):
            self.assertListEqual(row, list(b[j]))

    def test_cell_containing(self):
        """Test that the cell_containing method returns the correct thing"""
        a = [[0, 6, 0],
             [8, 0, 3],
             [0, 2, 0]]

        for loc in [(3, 3), (4, 3), (5, 3), (3, 4), (4, 4), (5, 4)]:
            b = Sudoku(solveable_list).cell_containing(*loc)

            for j, row in enumerate(a):
                self.assertListEqual(row, list(b[j]))

    def test_possible(self):
        """Test that possible works."""

        # in the example puzzle, a 5 is possible in the centre element
        # all others are not (i.e. the solution has a 5 there)

        s = Sudoku(solveable_list)
        for n in range(1, 10):
            if n == 5:
                self.assertTrue(s.possible(5, 4, 4))
            else:
                self.assertFalse(s.possible(n, 4, 4))

    def test_solved(self):
        """Test that my solution checker works."""

        # this is unsolved
        self.assertFalse(Sudoku(solveable_list).is_solved())

        # and this is solved
        presolved = [[5, 1, 3, 6, 8, 7, 2, 4, 9],
                     [8, 4, 9, 5, 2, 1, 6, 3, 7],
                     [2, 6, 7, 3, 4, 9, 5, 8, 1],
                     [1, 5, 8, 4, 6, 3, 9, 7, 2],
                     [9, 7, 4, 2, 1, 8, 3, 6, 5],
                     [3, 2, 6, 7, 9, 5, 4, 1, 8],
                     [7, 8, 2, 9, 3, 4, 1, 5, 6],
                     [6, 3, 5, 1, 7, 2, 8, 9, 4],
                     [4, 9, 1, 8, 5, 6, 7, 2, 3]]
        self.assertTrue(Sudoku(presolved).is_solved())


if __name__ == "__main__":
    unittest.main()
