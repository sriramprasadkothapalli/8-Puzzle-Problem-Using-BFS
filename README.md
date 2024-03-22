## 8-Puzzle Solver
This Python project implements a Breadth-First Search (BFS) algorithm to
solve the classic 8-puzzle problem.
**Instructions**
1. **Prerequisites:**
- Python 3 (https://www.python.org/downloads/)
- NumPy library: Install using `pip install numpy`
2. **Running the Code:**
- Save the Python code as a file (e.g.,
`proj1_sriramprasad_kothapalli.py`)
- Open a terminal or command prompt in the directory where you saved
the file.
- Execute the script: `python proj1_sriramprasad_kothapalli.py`
3. **Input:**
- **Within the code:** Modify the `input_matrix` and `goal_matrix`
variables in the `if __name__ == "__main__":` block to define your
starting puzzle configuration and the desired goal state.
- **Matrices:** Represent the puzzle as 3x3 NumPy arrays. The number
'0' represents the blank tile.
**Example:**
```python
input_matrix = np.array([[4, 7, 0], [1, 2, 8], [6, 3, 5]])
goal_matrix = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])
