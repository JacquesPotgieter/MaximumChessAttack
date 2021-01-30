class Position:
  def __init__(self, x, y, piece = None):
    self._x = x
    self._y = y
    self._piece = piece

  def print(self):
      position_name = self._piece.name() if self._piece else '. '
      print(" {} ".format(position_name), end='')
