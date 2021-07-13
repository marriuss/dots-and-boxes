import random
from .player import Player


class Bot(Player):
    def __init__(self, color, name):
        Player.__init__(self, color, name)
        self.type = "BOT"

    def make_move(self, game):
        current_state = game[-1]
        if current_state["gameover"]:
            self.terminal_state = True
            return None
        edge = random.sample(current_state["available_edges"], 1)[0][0]
        return edge
