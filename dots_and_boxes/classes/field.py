from .field_elements import Dot, Edge, Cell
from dots_and_boxes.settings import *


class Field:

    def __init__(self):
        self.edges = set()
        self.cells = []
        self.dots = []
        self.__create_dots()
        self.__create_edges()

    def __check_edge(self, dot1, dot2):
        check = list(filter(lambda e: e.dot1 is dot1 and e.dot2 is dot2, self.edges))
        if check:
            return check[0]
        else:
            return Edge(dot1, dot2)

    def __create_dots(self):
        for i in range(1, SIZE):
            for j in range(1, SIZE):
                d = Dot(i * CENTRE, j * CENTRE)
                self.dots.append(d)

    def __create_edges(self):
        i = 0
        for k in range((SIZE - 1) * (SIZE - 1)):
            if (k + 1) % (SIZE - 1) != 0 and k < (SIZE - 1) * (SIZE - 1) - SIZE:
                dot_tl = self.dots[k]
                dot_tr = self.dots[k + SIZE - 1]
                dot_bl = self.dots[k + 1]
                dot_br = self.dots[k + SIZE]
                e1 = self.__check_edge(dot_tl, dot_tr)
                e2 = self.__check_edge(dot_tl, dot_bl)
                e3 = self.__check_edge(dot_bl, dot_br)
                e4 = self.__check_edge(dot_tr, dot_br)
                self.edges.add(e1)
                self.edges.add(e2)
                self.edges.add(e3)
                self.edges.add(e4)
                self.cells.append(Cell((e1, e2, e3, e4)))
