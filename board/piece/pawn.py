from board.piece.piece import Piece

class Pawn(Piece):
  def __init__(self, *args):
    Piece.__init__(self, *args)

  def piece_letter(self):
    return 'p'

  def attack_positions(self, x, y):
    moves = [
      self.player().next_position(x, y, 1, 1),
      self.player().next_position(x, y, -1, 1)
    ]
    return [move for move in moves if move]
