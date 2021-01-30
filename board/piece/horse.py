from board.piece.piece import Piece

class Horse(Piece):
  def __init__(self, *args):
    Piece.__init__(self, *args)

  def piece_letter(self):
    return 'K'

  def attack_positions(self, x, y):
    moves = [
      self.player().next_position(x, y, 2, 1),
      self.player().next_position(x, y, 2, -1),
      self.player().next_position(x, y, -2, 1),
      self.player().next_position(x, y, -2, -1),
      self.player().next_position(x, y, 1, 2),
      self.player().next_position(x, y, 1, -2),
      self.player().next_position(x, y, -1, 2),
      self.player().next_position(x, y, -1, -2),
    ]
    return [move for move in moves if move]
