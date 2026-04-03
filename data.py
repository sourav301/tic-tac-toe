from enum import Enum
from game_observer import GameObserver 

class Symbol(Enum):
    CROSS = 'CROSS'
    CIRCLE = 'CIRCLE'
    EMPTY = 'EMPTY'

class Cell:
    def __init__(self, symbol: Symbol=Symbol.EMPTY):
        self.symbol = symbol
    def get_symbol(self):
        return self.symbol
    def set_symbol(self,symbol: Symbol):
        self.symbol = symbol

class Player:
    def __init__(self, name:str, symbol:Symbol):
        self.name = name
        self.symbol = symbol
        
    def get_symbol(self):
        return self.symbol

class Scoreboard(GameObserver):
    def __init__(self):
        self.scores = []
    def update(self, game):
        self.scores.append(game.winner.name)
        print("Scoreboard:",self.scores)

class InvalidMoveException(Exception):
    pass