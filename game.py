from board import Board
from data import InvalidMoveException, Player
from game_subject import GameSubject
from state import EndState, GameState, InProgressState
from winning_strategies import RowWinner


class Game(GameSubject):

    def __init__(self, size: int, player1: Player, player2: Player):
        super().__init__()
        self.board = Board(size)
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.state = InProgressState()
        self.winning_strategies = [RowWinner()]
        self.winner = None

    def make_move(self, row, col, player: Player):
        if self.current_player != player:
            raise InvalidMoveException("It is not your turn")
        self.state.make_move(self, row, col, player)

        if self.check_winner(player):
            print("winner- setting endstate")
            self.set_state(EndState())

    def switch_player(self):
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def check_winner(self, player):
        for strategies in self.winning_strategies:
            if strategies.check_winner(self.board, player):
                return True
        return False

    def set_state(self, state: GameState):
        self.state = state
        if self.winner:
            self.notify_observers()

    def get_state(self):
        return self.state
