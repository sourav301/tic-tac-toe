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


class ColWinner(WinningStrategy):
    def check_winner(self, board: Board, player: Player):
        for col in range(board.size):
            if all(
                board.get_cell(row, col).get_symbol() == player.get_symbol()
                for row in range(board.size)
            ):
                return True
        return False


class DiagonalWinner(WinningStrategy):
    def check_winner(self, board: Board, player: Player):
        symbol = player.get_symbol()
        size = board.size

        # Top-left → bottom-right
        main_diag = all(
            board.get_cell(i, i).get_symbol() == symbol for i in range(size)
        )

        # Top-right → bottom-left
        anti_diag = all(
            board.get_cell(i, size - 1 - i).get_symbol() == symbol for i in range(size)
        )

        return main_diag or anti_diag
