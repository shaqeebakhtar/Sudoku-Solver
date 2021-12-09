"""
    Program: Sudoku Solver
    Objective: To solve the given sudoku using BACKTRACKING METHOD
"""

# sudoku_grid = [
#     [9, 0, 0, 0, 0, 0, 1, 0, 6],
#     [0, 0, 0, 6, 2, 0, 7, 9, 0],
#     [0, 0, 5, 0, 0, 1, 0, 0, 0],
#     [5, 4, 0, 0, 0, 0, 0, 2, 0],
#     [8, 1, 0, 0, 6, 9, 3, 5, 7],
#     [3, 9, 0, 5, 8, 2, 6, 0, 4],
#     [6, 0, 0, 0, 0, 0, 0, 7, 0],
#     [0, 0, 9, 1, 5, 0, 0, 0, 3],
#     [2, 0, 3, 0, 4, 6, 0, 0, 0]
# ]

sudoku_grid = []

def make_grid():
    print("Enter Row as : 123456789")
    for i in range(9):
        lst = input(f"Enter Row - {i + 1} : ")
        row = [int(item) for item in lst]
        sudoku_grid.append(row)

def print_grid(grid):  # prints given list in a sudoku grid pattern
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(str(grid[i][j]))
            else:
                print(str(grid[i][j]), end=" ")

def find_empty(grid):  # find empty spaces in the sudoku grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return row, col

    return False

def valid_num(grid, num, pos):
    # checking row
    for i in range(len(grid)):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # checking row
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # checking the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(grid):
    empty = find_empty(grid)
    if not empty:  # if there is no empty space then already we have solved the sudoku
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if valid_num(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):  # we are checking the grid again with newly added value
                return True
            else:
                grid[row][col] = 0  # this will put 0 if not a valid num is found

    return False


make_grid()
print_grid(sudoku_grid)
solve(sudoku_grid)
print("\n--- Solved Sudoku ---\n")
print_grid(sudoku_grid)
