from functools import reduce

from dots_and_boxes.settings.colors import GRAY
import numpy as np


class Game:
    def __init__(self, players, cells, edges, gui):
        self.start_players = players
        self.cells = cells
        self.edges = edges
        self.gui = gui

    def reset(self):
        self.current_player = self.start_players[0]
        self.current_color = self.current_player.color
        self.current_players = self.start_players
        self.current_score = {pl: 0 for pl in self.start_players}
        for c in self.cells:
            c.reset()
        for e in self.edges:
            e.reset()
        for pl in self.start_players:
            pl.reset()
        self.is_gameover = False
        self.terminal_state = False
        self.win = None
        self.actions = []
        self.scores = [{pl: 0 for pl in self.start_players}]
        self.states = [self.get_current_state()]
        self.gui.draw_background()

    def get_available_edges(self):
        return list(filter(lambda e: not e.is_filled, self.edges))

    def get_available_cells(self):
        return list(filter(lambda c: not c.is_filled, self.cells))

    def get_current_state(self):
        return \
            {
                "cells": [c.cell() for c in self.cells],
                "edges": [e.edge() for e in self.edges],
                "available_cells": [c.cell() for c in self.get_available_cells()],
                "available_edges": [e.edge() for e in self.get_available_edges()],
                "scores": self.scores,
                "actions": self.actions,
                "current_player": self.current_player,
                "gameover": self.is_gameover,
                "win": self.win
            }

    def swap_players(self):
        self.current_players = np.roll(self.current_players, -1)
        self.current_player = self.current_players[0]
        self.current_color = self.current_player.color

    def check_gameover(self):
        self.is_gameover = not self.get_available_cells()
        if self.is_gameover:
            self.win_state()

    def win_state(self):
        win = max(self.current_score.items(), key=lambda x: x[1])
        color = win[0].color
        name = win[0].name
        score = win[1]
        self.win = (win[0], score)
        if score == len(self.cells) / 2:
            name = "DRAW"
            color = GRAY
            self.win = None
        self.gui.draw_win_text(name, score, color)

    def check_terminal_state(self):
        self.terminal_state = reduce(lambda x, y: x & y, map(lambda x: x.terminal_state, self.current_players))

    def do_action(self, edge):
        fl = False
        cells = list(filter(lambda c: c.contains(edge), self.get_available_cells()))
        for c in cells:
            c.make_edge(edge, self.current_color)
            if c.is_filled:
                self.current_score[self.current_player] += 1
                fl = True
        self.actions.append((self.current_player, edge))
        self.scores.append({pl: self.current_score[pl] for pl in self.start_players})
        if not fl:
            self.swap_players()
        self.check_gameover()
        self.states.append(self.get_current_state())

    def turn(self):
        edge = self.current_player.make_move(self.states)
        if edge is None:
            self.check_terminal_state()
            if not self.terminal_state:
                self.swap_players()
        else:
            self.do_action(edge)
            self.gui.update()
            self.gui.pause()

    def start(self):
        self.reset()

    def game(self):
        self.start()
        while not self.terminal_state:
            self.turn()
            self.gui.exit()
