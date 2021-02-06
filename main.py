from board import Board
from board.piece import Pawn, Horse, Bishop
from board.player import Player

from config import PLAYER_WHITE, PLAYER_BLACK

board = Board()

white = Player(PLAYER_WHITE)
black = Player(PLAYER_BLACK)

pawn_white = Pawn(white)
pawn_black = Pawn(black)
horse_black = Horse(black)
bishop_black = Bishop(black)

board.get(0, 0).assign_piece(pawn_white)
board.get(1, 1).assign_piece(pawn_black)
board.get(2, 0).assign_piece(pawn_white)
board.get(3, 2).assign_piece(horse_black)

board.get(3, 3).assign_piece(pawn_white)
board.get(4, 4).assign_piece(pawn_black)
board.get(5, 3).assign_piece(pawn_white)

board.get(6, 6).assign_piece(pawn_white)
board.get(7, 7).assign_piece(pawn_black)
board.get(6, 7).assign_piece(pawn_white)

board.get(4, 2).assign_piece(bishop_black)

board.print_board()
