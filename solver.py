def find_empty_location(grid):
    """Finds an empty location in the Sudoku grid (denoted by 0)"""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == "_":
                return (i, j)
    return None

def is_safe(grid, row, col, num):
    """Checks if placing a number at the given row and column is valid"""
    # Check row
    if num in grid[row]:
        return False
    # Check column
    if num in grid[:, col]:
        return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid, step=0):
    """Solves the Sudoku puzzle using backtracking"""
    print("Step:", step)
    print(grid)
    empty = find_empty_location(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_safe(grid, row, col, str(num)):
            grid[row][col] = str(num)
            if solve_sudoku(grid, step=step+1):
                return True
            grid[row][col] = "_"
    return False