from config import BOARD_HEIGHT, BOARD_WIDTH

class Board:
    def __init__(self):
      self._board = dict()
      for x in range(BOARD_HEIGHT):
          for y in range(BOARD_WIDTH):
              self._board[self.position_name(x, y)] = None

    def get(self, x, y):
        return self._board.get(self.position_name(x, y))

    def position_name(self, x, y):
        return "{}.{}".format(x, y)

    def print_board(self):
        self._print_line()
        for x in range(BOARD_WIDTH):
            print('# ', end='')
            for y in range(BOARD_HEIGHT):
                self._print_position(self.get(x, y))    
            print(' #')
        self._print_line()

        
    def _print_line(self):
        print('# ', end='')
        for _ in range(BOARD_WIDTH):
            print(' #  ',end='')
        print(' #')

    def _print_position(self, position):
        position_name = position.name() if position else '. '
        print(" {} ".format(position_name), end='')
