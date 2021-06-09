import random


class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.terminal_state = False
        self.type = "BOT"

    def make_move(self, game):
        current_state = game[-1]
        if current_state["gameover"]:
            self.terminal_state = True
            return None
        edge = random.sample(current_state["available_edges"], 1)[0][0]
        return edge

    def reset(self):
        self.terminal_state = False
