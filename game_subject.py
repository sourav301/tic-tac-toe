from game_observer import GameObserver


class GameSubject:
    def __init__(self):
        self.observers: list[GameObserver] = []

    def add_observer(self, observer: GameObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: GameObserver):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
