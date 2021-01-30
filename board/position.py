class Position:
  def __init__(self, x, y, piece = None):
    self._x = x
    self._y = y
    self._piece = piece

  def assign_piece(self, piece):
    self._piece = piece

  def player(self):
    return self._piece.player() if self._piece else None

  def attack_positions(self):
    return self._piece.attack_positions(self._x, self._y) if self._piece else []

  def can_attack(self, defender):
    if not (self._piece and defender._piece):
      return False
    if self.player() == defender.player():
      return False
    return True

  def print(self):
      position_name = self._piece.name() if self._piece else '. '
      print(" {} ".format(position_name), end='')
