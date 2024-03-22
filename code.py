import numpy as np
def print_board(board_data):
"""Prints the current state of the puzzle board in a formatted grid."""
for row_start in range(0, len(board_data), 3): # Iterate over rows
row = board_data[row_start : row_start + 3] # Extract row elements
print(f"| {row[0]} | {row[1]} | {row[2]} |") # Print formatted row
print('-------------') # Separator line
"""Funtions to perform the movements of the blank tile
Args:
puzzle: A list representation of the puzzle.
blank_index: The current index of the blank tile (0).
Returns: A tuple:
- The new puzzle state (list) if the move was possible, otherwise None.
- The new blank index if the move was possible, otherwise None.
- False (indicating the move was made)."""
def move_right(puzzle, blank_index):
size = int(np.sqrt(len(puzzle)))
if blank_index % size != size - 1: # Check if right move is valid
new_puzzle = puzzle.copy()
new_puzzle[blank_index], new_puzzle[blank_index + 1] =
new_puzzle[blank_index + 1], new_puzzle[blank_index]
return new_puzzle, blank_index + 1, True # Move was valid
else:
return puzzle, blank_index, False # Move invalid, return originals
# Function to perform left movement
def move_left(puzzle, blank_index):
size = int(np.sqrt(len(puzzle)))
if blank_index % size != 0: # Check if left move is valid
new_puzzle = puzzle.copy()
new_puzzle[blank_index], new_puzzle[blank_index - 1] =
new_puzzle[blank_index - 1], new_puzzle[blank_index]
return new_puzzle, blank_index - 1, True # Move was valid
else:
return puzzle, blank_index, False # Move invalid, return originals
# Function to perform up movement
def move_up(puzzle, blank_index):
size = int(np.sqrt(len(puzzle)))
if blank_index >= size: # Check if up move is valid
new_puzzle = puzzle.copy()
new_puzzle[blank_index], new_puzzle[blank_index - size] =
new_puzzle[blank_index - size], new_puzzle[blank_index]
return new_puzzle, blank_index - size, True # Move was valid
else:
return puzzle, blank_index, False # Move invalid, return originals
# Function to perform down movement
def move_down(puzzle, blank_index):
size = int(np.sqrt(len(puzzle)))
if blank_index < len(puzzle) - size: # Check if down move is valid
new_puzzle = puzzle.copy()
new_puzzle[blank_index], new_puzzle[blank_index + size] =
new_puzzle[blank_index + size], new_puzzle[blank_index]
return new_puzzle, blank_index + size, True # Move was valid
else:
return puzzle, blank_index, False # Move invalid, return originals
class PuzzleNode:
def __init__(self,blank_tile_position, parent_node, puzzlestate) :
self.blank_tile_position = blank_tile_position
self.parent_node = parent_node
self.puzzlestate = puzzlestate
class PuzzleState:
def __init__(self):
self.node_list = np.array([])
self.visited = np.array([])
self.not_visited = np.array([0])
self.states_list = np.array([])
# self.path = np.array([])
#Function to solve the puzzle using BFS algorithm
path = np.array([])
def solve_puzzle(puzzle, goal):
state = PuzzleState() # Create a new state object
puzzle = puzzle.T.flatten() # Flatten the puzzle to a 1D array
position = np.where(puzzle == 0)[0][0] # Get the position of the blank tile
state.node_list = np.append(state.node_list, PuzzleNode(position, None,
puzzle)) # Add the initial state to the node list
state.states_list = np.append(state.states_list, int("".join(map(str,
puzzle)))) # Add the initial state to the states list
goal = goal.T.flatten()
isGoal = False # Set the goal flag to False
puzzle_copy = puzzle.copy() # Create a copy of the puzzle
node_index = 0
parent = 0
counter = 0
# Loop through the puzzle until the goal state is reached
while not isGoal:
counter += 1
state.visited = np.append(state.visited, state.not_visited[0]) # Add the
current node to the visited list
state.not_visited = np.delete(state.not_visited, 0) # Remove the current
node from the not visited list
# Perform the movements
move_temporary, position_new, moved = move_down(puzzle_copy, position)
# Check if the move is valid and the state is not already visited
if moved and not isGoal and not (int("".join(map(str, move_temporary))) in
state.states_list):
# Add the new state to the node list and the states list
state.node_list = np.append(state.node_list, PuzzleNode(position_new,
parent, move_temporary))
# Add the new state to the states list
state.states_list = np.append(state.states_list, int("".join(map(str,
move_temporary))))
# Increment the node index
node_index += 1
# Check if the goal state is reached
if (goal == move_temporary).all():
isGoal = True
# Add the goal state to the not visited list
state.not_visited = np.append(state.not_visited, node_index)
# Perform the movements
move_temporary, position_new, moved = move_up(puzzle_copy, position)
if moved and not isGoal and not (int("".join(map(str, move_temporary))) in
state.states_list):
state.node_list = np.append(state.node_list, PuzzleNode(position_new,
parent, move_temporary))
state.states_list = np.append(state.states_list, int("".join(map(str,
move_temporary))))
# Increment the node index
node_index += 1
if (goal == move_temporary).all():
isGoal = True
state.not_visited = np.append(state.not_visited, node_index)
move_temporary, position_new, moved = move_right(puzzle_copy, position)
# Check if the move is valid and the state is not already visited
if moved and not isGoal and not (int("".join(map(str, move_temporary))) in
state.states_list):
state.node_list = np.append(state.node_list, PuzzleNode(position_new,
parent, move_temporary))
state.states_list = np.append(state.states_list, int("".join(map(str,
move_temporary))))
node_index += 1
if (goal == move_temporary).all():
isGoal = True
state.not_visited = np.append(state.not_visited, node_index)
move_temporary, position_new, moved = move_left(puzzle_copy, position)
# Check if the move is valid and the state is not already visited
if moved and not isGoal and not (int("".join(map(str, move_temporary))) in
state.states_list):
state.node_list = np.append(state.node_list, PuzzleNode(position_new,
parent, move_temporary))
state.states_list = np.append(state.states_list, int("".join(map(str,
move_temporary))))
node_index += 1
if (goal == move_temporary).all():
isGoal = True
state.not_visited = np.append(state.not_visited, node_index)
# Check if the not visited list is empty
if state.not_visited.size == 0:
print("Unsolvable Initial State")
break
# Set the new puzzle state, position, and parent
puzzle_node = state.node_list[state.not_visited[0]]
puzzle_copy = state.node_list[state.not_visited[0]].puzzlestate.copy()
position = puzzle_node.blank_tile_position.copy()
parent = state.not_visited[0]
# Print the solution
if isGoal:
global path
backtracker(state)
print("Solved!")
print("Number of nodes expanded: ", counter)
print("Path length: ", len(path))
# Save Path
with open('nodePath.txt', 'w') as file:
for num in reversed(path): # Reverse to get correct order
reshaped_num = num.reshape(3, 3) # Reshape to 3x3
for row in reshaped_num: # Iterate over rows
file.writelines('%s ' % str(item) for item in row) # Write row
elements
file.writelines('\n') # Newline after each row
file.writelines('\n') # Newline after each state
print_board(num)
# Save Nodes
with open('Nodes.txt', 'w') as file:
for node in state.node_list:
reshaped_state = node.puzzlestate.reshape(3, 3).T
flattened_state = reshaped_state.flatten()
file.writelines('%s ' % str(item) for item in flattened_state)
file.writelines('\n')
# Save Node Info
with open('NodesInfo.txt', 'w') as file:
file.write("Node_index\t Parent_Node_index\t\tNode\n") # Header
for index, node in enumerate(state.node_list):
file.write(str(index) + "\t\t\t")
file.write(str(node.parent_node) + '\t\t\t')
file.write("".join(map(str, node.puzzlestate.flatten())) + "\n")
# Function to backtrack the path
def backtracker(state):
index = -1 # Start at the index of the last node (goal state)
global path
path = np.array([state.node_list[-1].puzzlestate])
# Loop through the parent nodes until the initial state is reached
while state.node_list[index].parent_node is not None: # Loop until the initial
state is reached
index = state.node_list[index].parent_node # Set the index to the parent
node
path = np.append(path, [state.node_list[index].puzzlestate], axis=0) # Add
the parent node to the path
#Reverse to get correct order
# Main function to solve the puzzle
if __name__ == "__main__":
input_matrix = np.array([[4, 7, 0], [1, 2, 8], [6, 3, 5]]) # Test case 1
goal_matrix = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]]) # Goal State
solve_puzzle(input_matrix, goal_matrix)
