from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.terminal_state = False

    @abstractmethod
    def make_move(self, game):
        pass

    def reset(self):
        self.terminal_state = False
