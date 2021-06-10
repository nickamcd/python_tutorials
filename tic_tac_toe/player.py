import math
import random

class Player:
  def __init__(self, mark):
    # mark is either x or or
    self.mark = mark

  def get_move(self, game):
    pass

class RandomComputerPlayer(Player):
  def __init__(self, mark):
    super().__init__(mark)

  def get_move(self, game):
    cell = random.choice(game.available_moves())
    return cell

class HumanPlayer(Player):
  def __init__(self, mark):
    super().__init__(mark)
  
  def get_move(self, game):
    invalid_cell = True
    value = None
    while invalid_cell:
      cell = input(self.mark + '\'s turn. Input move(0-8): ')
      try:
        value = int(cell)
        if value not in game.available_moves():
          raise ValueError
        invalid_cell = False # chosen a valid invalid_square
      except ValueError:
        print('Invalid square. Try again.')
    
    return value

class MinMaxComputerPlayer(Player):
  def __init__(self, mark):
    super().__init__(mark)

  def get_move(self, game):
    if len(game.available_moves()) == 9:
      cell = random.choice(game.available_moves()) # random choice if all spaces empty
    else:
      cell = self.minimax(game, self.mark)['position']
    return cell

  def minimax(self, state, player):
    max_player = self.mark
    other_player = 'O' if player == 'X' else 'X'

    # base case
    if state.current_winner == other_player:
      return {
        'position': None,
        'score': 1 * (state.num_empty_cells() + 1) if other_player == max_player else -1 * (state.num_empty_cells() + 1)
      }
    elif not state.empty_cells(): # no winner
      return {
        'position': None,
        'score': 0
      }
    
    if player == max_player:
      best = {
        'position': None,
        'score': -math.inf # score should maximize
      }
    else:
      best = {
        'position': None,
        'score': math.inf # score should minimize
      }

    for possible_move in state.available_moves():
      # make move
      state.make_move(possible_move, player)
      # recurse using minimax to simulate game
      sim_score = self.minimax(state, other_player) # alternate player
      # undo move
      state.board[possible_move] = ' '
      state.current_winner = None
      sim_score['position'] = possible_move
      # update dictionaries if necessary
      if player == max_player:
        if sim_score['score'] > best['score']:
          best = sim_score
      else:
        if sim_score['score'] < best['score']:
          best = sim_score

    return best