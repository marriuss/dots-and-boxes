from .player import Player
import numpy.random as rand

import dots_and_boxes.settings.Q_learning


class Agent(Player):
    def __init__(self, color, name):
        Player.__init__(self, color, name)
        self.q_values = {}
        self.q_states = []
        self.keys = ["available_edges"]
        self.type = "AGENT"

    def make_move(self, game):
        current_state = game[-1]
        if current_state["gameover"]:
            self.terminal_state = True
            self.__Q_learning(game, 0.0)
            return None
        available_edges = current_state["available_edges"]
        fl = True
        for i, state in enumerate(self.q_states):
            fl = True
            for str in self.keys:
                if state[str] != current_state[str]:
                    fl = False
                    break
            if fl:
                index = i
                break
        if not fl or not self.q_states:
            self.q_states.append(current_state)
            index = len(self.q_states) - 1
        arr = rand.random_sample((len(available_edges),))
        dict_actions = self.q_values.setdefault(index, {e[0]: arr[i] for i, e in enumerate(available_edges)})
        best_action = max(dict_actions.items(), key=lambda x: x[1])
        if rand.random() < dots_and_boxes.settings.Q_learning.EPSILON:
            edge = rand.choice(list(dict_actions))
        else:
            edge = best_action[0]
        self.__Q_learning(game, best_action[1])
        return edge

    def __Q_learning(self, game, max_qvalue):
        current_state = game[-1]
        actions = current_state["actions"]
        scores = current_state["scores"]
        previous_state = None
        offset = -1
        buff = game[::-1][1:]
        if buff is None:
            return
        for i, st in enumerate(buff):
            if st["current_player"] is self:
                previous_state = st
                offset -= i
                break
        if previous_state is None:
            return
        index = -1
        for i, state in enumerate(self.q_states):
            fl = True
            for str in self.keys:
                if state[str] != previous_state[str]:
                    fl = False
                    break
            if fl:
                index = i
                break
        previous_score = scores[offset - 1]
        previous_action = actions[offset][1]
        current_score = scores[-1]
        players = current_score.keys()
        delta_score = {k: current_score[k] - previous_score[k] for k in players}
        reward = dots_and_boxes.settings.Q_learning.STEP_PENALTY
        for p in players:
            delta = delta_score[p]
            if p is self:
                reward += dots_and_boxes.settings.Q_learning.SCORE_BONUS * delta
            else:
                reward += dots_and_boxes.settings.Q_learning.OPPONENT_PENALTY * delta
        win = current_state["win"]
        if win is not None:
            if win[0] is self:
                reward += dots_and_boxes.settings.Q_learning.WIN_BONUS
            else:
                reward += dots_and_boxes.settings.Q_learning.LOSE_PENALTY
        current_qvalue = self.q_values[index][previous_action]
        new_qvalue = current_qvalue + dots_and_boxes.settings.Q_learning.ALPHA * (reward + dots_and_boxes.settings.Q_learning.GAMMA * max_qvalue - current_qvalue)
        self.q_values[index][previous_action] = new_qvalue
