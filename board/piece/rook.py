from board.piece.piece import Piece

class Rook(Piece):
  def __init__(self, *args):
    Piece.__init__(self, *args)

  def piece_letter(self):
    return 'R'

  def attack_positions(self, x, y):
    moves = []
    for i in range(8):
      moves.append(self.player().next_position(x, y, 1*i, 0))
      moves.append(self.player().next_position(x, y, -1*i, 0))
      moves.append(self.player().next_position(x, y, 0, -1*i))
      moves.append(self.player().next_position(x, y, 0, -1*i))
    return [move for move in moves if move]
