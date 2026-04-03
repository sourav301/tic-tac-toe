from data import Cell, InvalidMoveException, Player, Symbol


class Board:

    def __init__(self, size):
        self.size = size
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]

    def make_move(self, row, col, player: Player):
        if row < 0 or row >= self.size or col < 0 or col > self.size:
            raise InvalidMoveException(f"Please enter values with 0 and {self.size-1}")
        if self.board[row][col].get_symbol() != Symbol.EMPTY:
            raise InvalidMoveException("Cell is not empty")
        self.board[row][col].set_symbol(player.get_symbol())

    def get_cell(self, row, col) -> Symbol:
        return self.board[row][col]
