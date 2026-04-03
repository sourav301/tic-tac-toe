from abc import ABC, abstractmethod

from board import Board
from data import Player


class WinningStrategy(ABC):
    @abstractmethod
    def check_winner(self, board: Board, player: Player):
        pass


class RowWinner(WinningStrategy):
    def check_winner(self, board: Board, player: Player):
        for row in range(board.size):
            is_winner = True
            for col in range(board.size):
                if board.get_cell(row, col).get_symbol() != player.get_symbol():
                    is_winner = False
                    break
            if is_winner:
                return True
        return False
