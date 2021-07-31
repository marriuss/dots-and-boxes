from .classes import GUI, Game, Field
from .classes.players import Bot, Agent
from .settings import *


def main():

    gui = GUI()
    field = Field()

    # Players
    p1 = Bot(PURPLE, "Pavel")
    p2 = Agent(ROYAL_BLUE, "Sergei")
    p3 = Agent(MAGENTA, "Dmitriy")
    p4 = Bot(SPRING_GREEN_NEUTRAL, "Andrey")

    # Game setup
    players = [p1, p2, p3, p4]
    game = Game(players, field, gui)

    for i in range(0, EPISODE_AMOUNT):
        game.game()
        gui.pause(EPISODE_PAUSE)

    gui.exit()
