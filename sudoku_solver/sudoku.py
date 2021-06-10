def find_next_empty(puzzle):
  for r in range(9):
    for c in range(9):
      if puzzle[r][c] == -1:
        return r, c

  return None, None  

def is_valid(puzzle, guess, row, col):
  # check validity in row
  row_vals = puzzle[row]
  if guess in row_vals:
    return False

  # check validity in col
  col_vals = [puzzle[row][col] for row in range(9)]
  if guess in col_vals:
    return False

  # check validity in local square
  # find local square
  row_start = (row // 3) * 3
  col_start = (col // 3) * 3

  for r in range(row_start, row_start + 3):
    for c in range(col_start, col_start + 3):
      if puzzle[r][c] == guess:
        return False

  # passed all checks
  return True

def solve_sudoku(puzzle):
  # chose space to make guess
  row, col = find_next_empty(puzzle)

  # if all spaces filled, then done
  if row is None:
    return True

  # space is open, make a guess
  for guess in range(1, 10):
    # check validity of guess
    if is_valid(puzzle, guess, row, col):
      # place guess in puzzle
      puzzle[row][col] = guess
      # now perform recursion with this new puzzle
      if solve_sudoku(puzzle):
        return True

    # if not valid or if guess didn't solve puzzle
    # backtrack guess, try new number
    puzzle[row][col] = -1

  # No possible solution
  return False

if __name__ == '__main__':
  example_board = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]
  ]

  print(solve_sudoku(example_board))
  print(example_board)