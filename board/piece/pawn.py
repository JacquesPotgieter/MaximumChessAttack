from config import PLAYER_BLACK, PLAYER_WHITE
from board.piece.piece import Piece

class Pawn(Piece):
  def __init__(self, *args):
    Piece.__init__(self, *args)

  def name(self):
    return 'p'

  def attack_positions(self):
    moves = [
      self._point.move(1, 1),
      self._point.move(1, -1)
    ]
    return moves
