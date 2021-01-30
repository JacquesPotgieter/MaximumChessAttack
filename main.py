from board import Board
from board.piece import Pawn
from board.player import Player

from config import PLAYER_WHITE, PLAYER_BLACK

board = Board()

pawn_white = Pawn(Player(PLAYER_WHITE))
pawn_black = Pawn(Player(PLAYER_BLACK))

board.get(0, 0).assign_piece(pawn_white)
board.get(1, 1).assign_piece(pawn_black)
board.get(2, 0).assign_piece(pawn_white)

board.print_board()
