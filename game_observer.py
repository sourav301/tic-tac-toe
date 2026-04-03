from abc import ABC, abstractmethod


class GameObserver(ABC):
    @abstractmethod
    def update(self, message: str):
        pass
