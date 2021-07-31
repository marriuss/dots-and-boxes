from .player import Player
from dots_and_boxes.settings import GRAY


class Draw(Player):
    def __init__(self, score):
        Player.__init__(self, GRAY, "DRAW")
        self.type = "DRAW"
        self.score = score

    def make_move(self, game):
        pass
