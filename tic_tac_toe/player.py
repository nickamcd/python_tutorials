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