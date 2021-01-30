from config import BOARD_HEIGHT, BOARD_WIDTH
from board.position import Position

class Board:
    def __init__(self):
        self._board = dict()
        for y in range(BOARD_WIDTH):
            for x in range(BOARD_HEIGHT):
                self._board[self._position(x, y)] = Position(x, y, None)

    def get(self, x, y):
        return self._board.get(self._position(x, y))

    def _position(self, x, y):
        return "{}.{}".format(x, y)

    def print_board(self):
        self._print_line()
        for y in range(BOARD_HEIGHT):
            print('# ', end='')
            for x in range(BOARD_WIDTH):
                self.get(x, y).print()
            print(' #')
        self._print_line()

    def _print_line(self):
        print('# ', end='')
        for _ in range(BOARD_WIDTH):
            print(' #  ',end='')
        print(' #')


