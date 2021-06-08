class Edge:
    """
    Класс для представления границы клетки - единичного отрезка.
    """
    id = 0

    def __init__(self, dot1, dot2, gui):
        self.dot1 = dot1
        self.dot2 = dot2
        self.gui = gui
        self.color = None
        self.is_filled = False
        self.id = Edge.id
        Edge.id += 1

    def edge(self):
        """
        Возвращает основные свойства.
        """
        return self, self.is_filled, self.color

    def fill(self, color):
        """
        Перекрашивает ребро.
        """
        self.color = color
        self.is_filled = True
        self.gui.draw_line(self.color, (self.dot1.x, self.dot1.y), (self.dot2.x, self.dot2.y), 5)

    def reset(self):
        """
        Сбрасывает свойства ребра до начального состояния.
        """
        self.color = None
        self.is_filled = False