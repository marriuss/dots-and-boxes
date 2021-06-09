import random


class Player:
    """
    Класс для представления игрока.
    """

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.terminal_state = False
        self.type = "BOT"

    def make_move(self, game):
        """
        Принимает решение о действии на основе информации о состояниях игры.
        """
        current_state = game[-1]
        if current_state["gameover"]:
            self.terminal_state = True
            return None
        edge = random.sample(current_state["available_edges"], 1)[0][0]
        return edge

    def reset(self):
        """
        Сбрасывает свойства игрока до начального состояния.
        """
        self.terminal_state = False
