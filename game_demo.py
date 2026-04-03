from data import Player, Symbol
from ticTacToeSystem import TicTacToeSystem


class GameDemo:
    @staticmethod
    def game():
        tickTacToeSystem = TicTacToeSystem()

        player1 = Player("Sourav", Symbol.CIRCLE)
        player2 = Player("Koyel", Symbol.CROSS)
        tickTacToeSystem.create_game(3, player1=player1, player2=player2)
        tickTacToeSystem.make_move(0, 0, player1)
        tickTacToeSystem.make_move(1, 0, player2)

        tickTacToeSystem.make_move(0, 1, player1)
        tickTacToeSystem.make_move(1, 1, player2)

        tickTacToeSystem.make_move(0, 2, player1)
        # tickTacToeSystem.make_move(1,2,player2)


GameDemo.game()
