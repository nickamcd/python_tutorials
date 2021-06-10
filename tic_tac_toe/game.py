from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
  def __init__(self):
    self.board = [' ' for i in range(9)]
    self.current_winner = None

  def print_board(self):
    for row in [self.board[(i * 3) : ((i + 1) * 3)] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')

  @staticmethod
  def print_board_numbers():
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')
    
  def available_moves(self):
    return [i for i, cell in enumerate(self.board) if cell == ' ']
    # moves = []
    # for (i, cell) in enumerate(self.board):
    #   if cell == ' ':
    #     moves.append(i)
    # return moves

  def empty_cells(self):
    return ' ' in self.board

  def num_empty_cells(self):
    return len(self.available_moves())

  def make_move(self, cell, mark):
    if self.board[cell] == ' ':
      self.board[cell] = mark
      if self.winner(cell, mark):
        self.current_winner = mark
      return True
    return False

  def winner(self, cell, mark):
    # check row
    row_index = cell // 3
    row = self.board[row_index * 3 : (row_index + 1) * 3]
    if all([space == mark for space in row]):
      return True

    # check col
    col_index = cell % 3
    col = [self.board[(col_index + (i * 3))] for i in range(3)]
    if all([space == mark for space in col]):
      return True

    # check diagonals
    if cell % 2 == 0:
      diagonal1 = [self.board[i] for i in [0, 4, 8]] # top left to bot right
      if all([space == mark for space in diagonal1]):
        return True
      diagonal2 = [self.board[i] for i in [2, 4, 6]] # top right to bot left
      if all([space == mark for space in diagonal2]):
        return True

    #if all checks fail
    return False

def play(game, x_player, o_player, print_game=True):
  if print_game:
    game.print_board_numbers()

  mark = 'X' # starting player

  while game.empty_cells():
    if mark == 'O':
      cell = o_player.get_move(game)
    else:
      cell = x_player.get_move(game)

    if game.make_move(cell, mark):
      if print_game:
        print(mark + f' makes a move to cell {cell}')
        game.print_board()
        print('')

      if game.current_winner:
        if print_game:
          print(game.current_winner)
          print(mark + ' wins!')
        return mark
      
      mark = 'X' if mark == 'O' else 'O'

  if print_game:
    print('It\'s a tie!')

if __name__ == '__main__':
  x_player = HumanPlayer('X')
  o_player = RandomComputerPlayer('O')
  t = TicTacToe()
  play(t, x_player, o_player, print_game=True)