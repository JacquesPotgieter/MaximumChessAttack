from config import PLAYER_BLACK, BOARD_WIDTH, BOARD_HEIGHT

class Player:
  def __init__(self, color):
    self._color = color

  def color(self):
    return self._color

  def next_position(self, current_x, current_y, move_x, move_y):
    if self._color == PLAYER_BLACK:
      move_y = move_y * -1 # Black moves from bottom up
    new_x = current_x + move_x
    new_y = current_y + move_y

    if new_x < 0 or new_x >= BOARD_WIDTH:
      return None
    if new_y < 0 or new_y >= BOARD_HEIGHT:
      return None
    return (new_x, new_y)
