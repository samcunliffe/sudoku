"""
solvers.py

The actual solving functions.
"""


def solve_computerphile(s):
    """Solve the sudoku puzzle with backtracking and a DEEP nested loop.
    https://youtu.be/G_UYXzGuqvM

    Doesn't do anything fancy, just prints the solution and looks for the next.

    Parameters:
        s (sudoku.Sudoku): the unsolved puzzle
    """
    for i in range(9):
        for j in range(9):
            if s.arr[j][i] == 0:
                for n in range(1, 10):
                    if s.possible(n, i, j):
                        s.arr[j][i] = n
                        solve_computerphile(s=s)
                        s.arr[j][i] = 0
                return
    print(s)
    return
