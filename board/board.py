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

    def attack_value(self):
        attack = 0
        for y in range(BOARD_WIDTH):
            for x in range(BOARD_HEIGHT):
              attack = attack + self.attack_per_position(self.get(x, y))
        return attack

    def attack_per_position(self, attacker):
        attack_value = 0
        for (x, y) in attacker.attack_positions():
            defender = self.get(x, y)
            if attacker.can_attack(defender):
                attack_value = attack_value + 1
        return attack_value

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
        print("Attack = {}".format(self.attack_value()))
        print('')

    def _print_line(self):
        print('# ', end='')
        for _ in range(BOARD_WIDTH):
            print(' #  ',end='')
        print(' #')


