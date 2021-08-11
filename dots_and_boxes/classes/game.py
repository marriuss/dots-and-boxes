from functools import reduce
import numpy as np
from .players import Draw
from .state_components import StateComponent


class Game:
    def __init__(self, players, field, gui):
        self.__start_players = players
        self.cells = field.cells
        self.edges = field.edges
        self.__gui = gui
        self.current_players = None
        self.current_player = None
        self.current_color = None
        self.current_score = None
        self.is_gameover = None
        self.terminal_state = None
        self.win = None
        self.actions = None
        self.scores = None
        self.states = None

    def __reset(self):
        self.current_players = self.__start_players
        self.current_player = self.current_players[0]
        self.current_color = self.current_player.color
        self.current_score = {pl: 0 for pl in self.__start_players}
        for c in self.cells:
            c.reset()
        for e in self.edges:
            e.reset()
        for pl in self.__start_players:
            pl.reset()
        self.is_gameover = False
        self.terminal_state = False
        self.win = None
        self.actions = []
        self.scores = [{pl: 0 for pl in self.__start_players}]
        self.states = [self.__get_current_state()]
        self.__gui.draw_background()

    def __get_available_edges(self):
        return list(filter(lambda e: not e.is_filled, self.edges))

    def __get_available_cells(self):
        return list(filter(lambda c: not c.is_filled, self.cells))

    def __get_current_state(self):
        return \
            {
                "cells": [c.cell() for c in self.cells],
                "edges": [e.edge() for e in self.edges],
                "available_cells": [c.cell() for c in self.__get_available_cells()],
                "available_edges": [e.edge() for e in self.__get_available_edges()],
                "scores": self.scores,
                "actions": self.actions,
                "current_player": self.current_player,
                "gameover": self.is_gameover,
                "win": self.win
            }

    def __swap_players(self):
        self.current_players = np.roll(self.current_players, -1)
        self.current_player = self.current_players[0]
        self.current_color = self.current_player.color

    def __check_gameover(self):
        self.is_gameover = not self.__get_available_cells()
        if self.is_gameover:
            self.__win_state()

    def __win_state(self):
        max_score = max(self.current_score.values())
        win_players = list(filter(lambda p: p.score == max_score, self.__start_players))
        if len(win_players) > 1:
            winner = Draw(max_score)
            self.win = None
        else:
            winner = win_players[0]
            self.win = (winner, max_score)
        self.__gui.draw_win_text(winner)

    def __check_terminal_state(self):
        self.terminal_state = reduce(lambda x, y: x & y, map(lambda x: x.terminal_state, self.current_players))

    def __do_action(self, edge):
        fl = False
        cells = list(filter(lambda c: c.contains(edge), self.__get_available_cells()))
        for c in cells:
            c.make_edge(edge, self.current_color, self.__gui)
            if c.is_filled:
                self.current_score[self.current_player] += 1
                self.current_player.increase_score()
                fl = True
        self.actions.append((self.current_player, edge))
        self.scores.append({pl: self.current_score[pl] for pl in self.__start_players})
        if not fl:
            self.__swap_players()
        self.__check_gameover()
        self.states.append(self.__get_current_state())

    def __turn(self):
        edge = self.current_player.make_move(self.states)
        if edge is None:
            self.__check_terminal_state()
            if not self.terminal_state:
                self.__swap_players()
        else:
            self.__do_action(edge)
            self.__gui.update()
            self.__gui.pause()

    def __start(self):
        self.__reset()

    def game_loop(self):
        self.__start()
        while not self.terminal_state:
            self.__turn()
            self.__gui.exit()
