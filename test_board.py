import unittest

from board import Board
from data import InvalidMoveException, Player, Symbol


class TestBoardMakeMove(unittest.TestCase):

    def setUp(self):
        self.board = Board(3)
        self.player1 = Player("Alice", Symbol.CROSS)

    def test_valid_move(self):
        """Test that a valid move can be made on an empty cell"""
        self.board.make_move(0, 0, self.player1)
        cell = self.board.get_cell(0, 0)
        self.assertEqual(cell.get_symbol(), Symbol.CROSS)


if __name__ == "__main__":
    unittest.main()
