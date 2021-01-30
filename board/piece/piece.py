from config import BOARD_WIDTH, BOARD_HEIGHT

class Piece(object):
  def __init__(self, player):
    self._player = player

  def attack_positions(self, x, y):
    raise NotImplementedError('Override this method')

  def player(self):
    return self._player

  def name(self):
    return "{}{}".format(self.piece_letter(), self._player.color())

  def piece_letter(self):
    raise NotImplementedError('Override this method')