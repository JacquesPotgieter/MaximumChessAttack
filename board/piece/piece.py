from config import BOARD_WIDTH, BOARD_HEIGHT

class Piece(object):
  def __init__(self, player):
    self._player = player

  def next_possible_positions(self):
    raise NotImplementedError('Override this method')

  def name(self):
    return "{}{}".format(self.piece_letter(), self._player.letter())

  def piece_letter(self):
    raise NotImplementedError('Override this method')