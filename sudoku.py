"""
sudoku.py

A wrapper class for a 9*9 numpy array. Makes the input checking a bit nicer
and gives me the option to have fancy printing.
"""

import numpy as _np


class Sudoku:
    """A valid sudoku puzzle stored as a 9*9 numpy array"""

    def __init__(self, arr):
        """Initialise the Sudoku object"""
        self.arr = _np.array(arr)
        if self.arr.shape != (9, 9):
            raise TypeError('A Sudoku must be 9*9')
        if self.arr.dtype is not _np.dtype('int64'):
            raise TypeError('A Sudoku must be an array of integers')

    def __str__(self):
        """Nice terminal view with cells separated"""
        out = ""
        for j, row in enumerate(self.arr):
            if j in [3, 6]:
                out += "------+-------+------\n"
            fullrow = str(row)[1:-1].replace("0", " ")
            out += fullrow[:5] + " |" + \
                fullrow[5:11] + " |"+fullrow[11:] + "\n"
        return out

    def row(self, j):
        """Get a row

        Parameters:
            j (int): the row number

        Returns:
            the jth row
        """
        return self.arr[j]

    def column(self, i):
        """Get a column

        Parameters:
            i (int): the column number

        Returns:
            the ith column
        """
        return self.arr[:, i]

    def cell(self, k):
        """Get a 3*3 cell

        Parameters:
            k (int): the cell number

        Returns:
            the kth cell
        """
        iI = k % 3  # the cell's column number (in the 3*3 supergrid)
        jJ = k//3  # the cell's row number (in the 3*3 supergrid)
        return self.arr[3*jJ:3*jJ+3, iI*3:iI*3+3]

    def cell_containing(self, i, j):
        """Get a 3*3 cell containing the index (i, j)

        Parameters:
            i (int): the column number
            j (int): the row number

        Returns:
            the cell
        """
        k = (i//3)+3*(j//3)
        return self.cell(k)

    def possible(self, n, i, j):
        """Is the digit n possible in entry (i, j)

        Parameters:
            n (int): the trial digit
            i (int): the column number
            j (int): the row number

        Returns:
            bool: True if possible
        """
        if self.arr[j][i] != 0:
            return False

        # possible in the column
        if n in self.column(i):
            return False

        # possible in the row
        if n in self.row(j):
            return False

        # possible in the cell
        if n in self.cell_containing(i, j):
            return False

        return True

    def is_solved(self):
        """Check if this sudoku is solved

        Returns:
            True if solved.
        """

        ns = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        cols = [(ns == set(self.column(i).tolist())) for i in range(9)]
        rows = [(ns == set(self.row(i).tolist())) for i in range(9)]
        cels = [(ns == set(self.cell(i).flatten().tolist())) for i in range(9)]

        return all(cols+rows+cels)
