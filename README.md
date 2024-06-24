# Sudoku Generator and Solver

Run `python main.py` in the terminal and a small 9x9 Sudoku will be generated then solved using a [backtracking algorithm](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms).

![](Head.png)

### ✨ Main Features
+ `sudoku.fill()` to fill an empty grid with numbers that follow the rules of Sudoku.
+ `sudoku.delete()` to randomly delete numbers out of the grid to turn it into a puzzle.
+ `sudoku.show()` to display the sudoku visually using [matplotlib]() just like in the image above.
+ `sudoku.save_text()` to save a sudoku as a text file.
---
+ `solver.solve_sudoku()` to find the solution for a given Sudoku.

---
### Neural and Neurosymbolic Solvers
See [Kyubyong's Sudoku implementation](https://github.com/Kyubyong/sudoku). It proposes a neural network solver for Sudoku tasks. There is plenty of other code and research on the subject as well. I have a few related questions:

**1st question**: What variation of Sudoku would require a neural network in order to be solvable in a reasonable time? Scaled up size and more numbers?

**2nd question**: Can an AI learn the rules from Sudoku and execute them systematically
+ without any instructions in form of rules but
+ only given the smallest set of possible examples? 

This problem is similar to the [Abstraction and Reasoning Challenge](https://arcprize.org/) yet more focused on chains of mathematical reasoning which truly requires code synthesis rather than inferring rules based on core-knowledge and only implementing them manually a few times. 

It is also similar to [Alpha Geometry](https://www.nature.com/articles/s41586-023-06747-5) as the goal is to find the right chain of operations to solve/complete the puzzle but with the added challenge of understanding the rules of the game given examples in the first place. 

I believe it is important to 
+ A) minimize the amount of examples from which the rules of the game or program are inferred, and
+ B) to maximize the amount of steps an AI has to execute and reason through systematically in order to solve a new puzzle that abides to the same rules.