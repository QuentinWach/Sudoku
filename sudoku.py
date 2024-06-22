import numpy as np
import matplotlib.pyplot as plt

class sudoku():
    """ A general sudoku creator of arbitrary size. """

    def __init__(self):
        self.grid = np.zeros((9,9), dtype=str)

    def fill(self, id=42):
        np.random.seed(id)  # Set the seed for reproducibility
        numbers = np.arange(1, 10)  # Generate an array of numbers from 1 to 9
        np.random.shuffle(numbers)  # Shuffle the numbers randomly
        for i in range(9):
            for j in range(9):
                self.grid[i, j] = numbers[(i*3 + i//3 + j) % 9]

    def is_full(self):
        return "_" not in self.grid
    
    def missing(self, i, j):
        # Find the missing numbers in the row, column and subgrid
        row = set(self.grid[i, :])
        col = set(self.grid[:, j])
        subgrid = set(self.grid[(i//3)*3:(i//3)*3+3, (j//3)*3:(j//3)*3+3].flatten())
        missing = set(str(x) for x in range(1, 10)) - row - col - subgrid
        return list(missing)
    
    def missing_in_row(self, i):
        row = set(self.grid[i, :])
        missing = set(str(x) for x in range(1, 10)) - row
        return list(missing)

    def missing_in_column(self, j):
        col = set(self.grid[:, j])
        missing = set(str(x) for x in range(1, 10)) - col
        return list(missing)
    
    def missing_in_subgrid(self, i, j):
        subgrid = set(self.grid[(i//3)*3:(i//3)*3+3, (j//3)*3:(j//3)*3+3].flatten())
        missing = set(str(x) for x in range(1, 10)) - subgrid
        return list(missing)
    
    def delete(self, n, id=42):
        np.random.seed(id)  # Set the seed for reproducibility
        for _ in range(n):
            i = np.random.randint(9)
            j = np.random.randint(9)
            self.grid[i, j] = "_"

    def show(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        # Draw the grid lines
        for x in range(10):
            # Thick lines for 3x3 subgrids
            if x % 3 == 0:
                ax.axhline(x, xmin=0.049, xmax=0.953, color='black', linewidth=2.5)
                ax.axvline(x, ymin=0.049, ymax=0.953, color='black', linewidth=2.5)
            else:
                ax.axhline(x, xmin=0.049, xmax=0.953, color='black', linewidth=0.5)
                ax.axvline(x, ymin=0.049, ymax=0.953, color='black', linewidth=0.5)
        # Hide the axes
        ax.axis('off')
        # Place the numbers in the grid
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] != 0:
                    if self.grid[i, j] == "_":
                        ax.text(j + 0.5, 8.5 - i, "",
                            ha='center', va='center', fontsize=16)
                    else:   
                        ax.text(j + 0.5, 8.5 - i, str(self.grid[i, j]),
                                ha='center', va='center', fontsize=16)
        plt.tight_layout()
        plt.show()

    def text(self):
        print(self.grid)
        print("\n")

    def save_text(self, filename):
        # Generate the output file
        with open(filename+".txt", "w") as f:
            for i in range(9):
                for j in range(9):
                    f.write(str(self.grid[i, j]))
                    if j < 8:
                        f.write(" ")
                if i < 8:
                    f.write("\n")
