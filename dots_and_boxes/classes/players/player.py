import random


class Player:
    """
    Класс для представления игрока.
    """

    def __init__(self, color, name):
        self.color = color  # установка цвета игрока
        self.name = name  # установка имени игрока
        self.terminal_state = False  # работа игрока не завершена
        self.type = "BOT"  # тип игрока - бот

    def make_move(self, game):
        """
        Принимает решение о действии на основе информации о состояниях игры.
        """
        current_state = game[-1]  # текущее состояние
        if current_state["gameover"]:  # если игра уже закончена
            self.terminal_state = True  # работа игрока завершена
            return None
        edge = random.sample(current_state["available_edges"], 1)[0][0]  # случайный выбор из доступных действий
        return edge

    def reset(self):
        """
        Сбрасывает свойства игрока до начального состояния.
        """
        self.terminal_state = False
