from __future__ import annotations

from abc import ABC, abstractmethod

from data import InvalidMoveException


class GameState(ABC):

    @abstractmethod
    def make_move(self, game: Game):  # type: ignore
        pass


class InProgressState(GameState):
    name = "InProgressState"

    def make_move(self, game: Game, row, col, player):  # type: ignore
        game.board.make_move(row, col, player)
        if game.check_winner(player):
            game.set_state(EndState())
            game.winner = player
        else:
            game.switch_player()


class EndState(GameState):
    name = "EndState"

    def make_move(self, game, row, col, player):
        raise InvalidMoveException("Game has ended. Please restart.")
