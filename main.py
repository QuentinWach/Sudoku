import numpy as np
import matplotlib.pyplot as plt
from sudoku import sudoku
from solver import *

if __name__ == "__main__":
    # Generate and save a sudoku puzzle
    id = 42 # Seed
    A = sudoku()
    A.fill(id=id)
    A.show()
    A.delete(9*9, id=id)
    A.show()
    A.save_text("sudoku")

    # Solve the sudoku through backtracking
    solve_sudoku(A.grid)
    A.show()
    A.save_text("solution")