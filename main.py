from board import Board
from board.piece import Pawn
from board.player import Player

board = Board()
board.print_board()

pawn = Pawn(Player('w'))
board.get(1, 1).assign_piece(pawn)

board.print_board()
