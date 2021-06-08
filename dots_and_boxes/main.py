from dots_and_boxes.classes.GUI import GUI
from dots_and_boxes.classes.field_elements.dot import Dot
from dots_and_boxes.classes.field_elements.edge import Edge
from dots_and_boxes.classes.field_elements.cell import Cell
from dots_and_boxes.classes.players.player import Player
from dots_and_boxes.classes.players.agent import Agent
from dots_and_boxes.classes.game import Game
from dots_and_boxes.settings.colors import *
from dots_and_boxes.settings.GUI_settings import *
from dots_and_boxes.settings.game import *

gui = GUI()


def check_edge(dot1, dot2, edges):
    """
    Проверяет, был ли уже создан отрезок с такими точками.
    """
    check = list(filter(lambda e: e.dot1 is dot1 and e.dot2 is dot2, edges))
    if check:
        return check[0]
    else:
        return Edge(dot1, dot2, gui)


def main():
    edges = set()
    cells = []
    dots = []
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            d = Dot(i * CENTRE, j * CENTRE)
            dots.append(d)

    i = 0
    for k in range((SIZE - 1) * (SIZE - 1)):
        if (k + 1) % (SIZE - 1) != 0 and k < (SIZE - 1) * (SIZE - 1) - SIZE:
            dot_tl = dots[k]
            dot_tr = dots[k + SIZE - 1]
            dot_bl = dots[k + 1]
            dot_br = dots[k + SIZE]
            e1 = check_edge(dot_tl, dot_tr, edges)
            e2 = check_edge(dot_tl, dot_bl, edges)
            e3 = check_edge(dot_bl, dot_br, edges)
            e4 = check_edge(dot_tr, dot_br, edges)
            edges.add(e1)
            edges.add(e2)
            edges.add(e3)
            edges.add(e4)
            cells.append(Cell((e1, e2, e3, e4), gui))

    # Players
    p1 = Player(PURPLE, "Pavel")
    p2 = Agent(ROYAL_BLUE, "Sergei")
    p3 = Agent(MAGENTA, "Dmitriy")

    # Game setup
    players = [p1, p2, p3]
    game = Game(players, cells, edges, gui)

    for i in range(0, EPISODE_AMOUNT):
        game.game()
        gui.pause(EPISODE_PAUSE)

    gui.exit()
