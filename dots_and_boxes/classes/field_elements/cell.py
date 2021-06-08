class Cell:
    """
    Класс для представления клетки.
    """

    def __init__(self, edges, gui):
        self.possible_edges = set(edges)  # границы клетки
        self.centre(edges[0], edges[2])  # определения центра клетки
        self.edges = set()  # множество уже отмеченных границ клетки
        self.is_filled = False  # клетка не отмечена
        self.color = None  # клетка не имееет цвета
        self.gui = gui

    def make_edge(self, edge, color):
        """
        Перекрашивает одну из неотмеченных границ.
        """
        if not self.is_filled:  # если сама клетка еще не была покрашена
            # если данный отрезок принадлежит клетке и еще не был покрашен
            if self.contains(edge) and edge not in self.edges:
                self.edges.add(edge)  # клетка запоминает свои покрашенных границы
                edge.fill(color)  # сам отрезок должен быть отмечен
                if len(self.edges) == 4:  # все границы клетки покрашены
                    self.fill(color)  # клетка становится меченной

    def cell(self):
        """
        Возвращает основные свойства клетки.
        """
        return self, self.is_filled, self.color

    def fill(self, color):
        """
        Перекрашивает клетку.
        """
        self.is_filled = True  # клетка отмечена
        self.color = color  # установка цвета
        self.gui.draw_dot(self.color, self.centre)  # отрисовка отметки

    def centre(self, top, bottom):
        """
        Просчитывает координаты центра клетки.
        """
        l_corner = (top.dot1.x, top.dot1.y)  # координата левого угла
        r_corner = (bottom.dot2.x, bottom.dot2.y)  # координата правого угла
        self.centre = ((l_corner[0] + r_corner[0]) / 2, (l_corner[1] + r_corner[1]) / 2)  # координата центра клетки

    def contains(self, edge):
        """
        Проверяет, является ли границей клетки.
        """
        return edge in self.possible_edges

    def reset(self):
        """
        Сбрасывает свойства клетки до начального состояния.
        """
        self.is_filled = False
        self.color = None
        self.edges = set()
