from board.piece.piece import Piece

class Bishop(Piece):
  def __init__(self, *args):
    Piece.__init__(self, *args)

  def piece_letter(self):
    return 'B'

  def attack_positions(self, x, y):
    moves = []
    for i in range(8):
      moves.append(self.player().next_position(x, y, 1*i, 1*i))
      moves.append(self.player().next_position(x, y, -1*i, 1*i))
      moves.append(self.player().next_position(x, y, 1*i, -1*i))
      moves.append(self.player().next_position(x, y, -1*i, -1*i))
    return [move for move in moves if move]
