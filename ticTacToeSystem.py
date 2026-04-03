from threading import Lock
from data import Scoreboard, Player
from game import Game

class TicTacToeSystem:
    instance = None
    initialized = False
    lock = Lock()
    def __new__(cls):
        with cls.lock:
            if not cls.instance:
                cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self):
        if not self.initialized:
            self.initialized = True
            self.game = None
            self.scoreboard = Scoreboard()
    
    @classmethod
    def get_instance(cls):
        return cls()

    def create_game(self, size:int, player1: Player, player2: Player):
        self.game = Game(size, player1, player2)
        self.game.add_observer(self.scoreboard)
    
    def make_move(self, row, col, player):
        self.game.make_move(row, col, player)
    