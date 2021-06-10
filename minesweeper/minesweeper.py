import random
import re

class Board:
  def __init__(self, grid_size, num_bombs):
    self.grid_size = grid_size
    self.num_bombs = num_bombs

    # create board
    self.board = self.make_new_board()
    self.assign_values_to_board()

    # initialize set to track locations that have been dug
    # save as (row, col) tuples into set
    self.dug = set()

  def make_new_board(self):
    board = [[None for i in range(self.grid_size)] for i in range(self.grid_size)]

    bombs_planted = 0
    while bombs_planted < self.num_bombs:
      location = random.randint(0, self.grid_size**2 - 1)
      row = location // self.grid_size
      col = location % self.grid_size

      if board[row][col] == '*':
        # bomb already planted in this location
        continue

      board[row][col] = '*'
      bombs_planted += 1

    return board

  def assign_values_to_board(self):
    for row in range(self.grid_size):
      for col in range(self.grid_size):
        if self.board[row][col] == '*':
          # already a bomb, no calculation needed 
          continue
        self.board[row][col] = self.get_num_neighboring_bombs(row, col)

  def get_num_neighboring_bombs(self, row, col):
    num_neighboring_bombs = 0
    for r in range(max(0, row - 1), min(self.grid_size - 1, row + 1) + 1):
      for c in range(max(0, col - 1), min(self.grid_size - 1, col + 1) + 1):
        if r == row and c == col:
          # original location
          continue
        if self.board[r][c] == '*':
          num_neighboring_bombs += 1
    return num_neighboring_bombs

  def dig(self, row, col):

    self.dug.add((row, col)) # log location into set

    if self.board[row][col] == '*':
      return False
    elif self.board[row][col] > 0:
      return True

    for r in range(max(0, row - 1), min(self.grid_size - 1, row + 1) + 1):
      for c in range(max(0, col - 1), min(self.grid_size - 1, col + 1) + 1):
        if (r, c) in self.dug:
          # already dug
          continue
        self.dig(r, c)

    return True

  def __str__(self):
    # define __str__
    visible_board = [[None for i in range(self.grid_size)] for i in range(self.grid_size)]
    for row in range(self.grid_size):
      for col in range(self.grid_size):
        if (row, col) in self.dug:
          visible_board[row][col] = str(self.board[row][col])
        else:
          visible_board[row][col] = ' '


    string_rep = ''
    widths = []
    for idx in range(self.grid_size):
      columns = map(lambda x: x[idx], visible_board)
      widths.append(len(max(columns, key = len)))

    indices = [i for i in range(self.grid_size)]
    indices_row = '   '
    cells = []
    for idx, col in enumerate(indices):
      format = '%-' + str(widths[idx]) + "s"
      cells.append(format % (col))
    indices_row += '  '.join(cells)
    indices_row += ' \n'

    for i in range(len(visible_board)):
      row = visible_board[i]
      string_rep += f'{i} |'
      cells = []
      for idx, col in enumerate(row):
        format = '%-' + str(widths[idx]) + "s"
        cells.append(format % (col))
      string_rep += ' |'.join(cells)
      string_rep += ' |\n'

    str_len = int(len(string_rep) / self.grid_size)
    string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

    return string_rep

def play(grid_size=10, num_bombs=10):
  # create board and plant bombs
  board = Board(grid_size, num_bombs)
  # show user board and ask where to dig

  # if location is bomb show game over message
  # if location is not bomb, dig recursively until next to bombs
  # repeat until no more places to dig
  
  while len(board.dug) < board.grid_size ** 2 - num_bombs:
    print(board)
    user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
    row, col = int(user_input[0]), int(user_input[-1])
    if row < 0 or row >= board.grid_size or col < 0 or col >= board.grid_size:
      print("Invalid location. Try again.")
      continue

    safe = board.dig(row, col)
    if not safe:
      break # game over

  if safe:
    print('Congratulations, you win!')
  else:
    print('Game Over')
    board.dug = [(r, c) for r in range(board.grid_size) for c in range(board.grid_size)]
    print(board)
  
if __name__ == '__main__':
  play()