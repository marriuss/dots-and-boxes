from dots_and_boxes.classes.players.player import *
import numpy.random as rand

from dots_and_boxes.settings.Q_learning import *


class Agent(Player):
    """
    Класс для представления интеллектуального агента.
    """

    def __init__(self, color, name):
        Player.__init__(self, color, name)
        self.q_values = {}  # хэш-таблица для хранения Q-значений
        self.q_states = []  # список уже найденных агентом состояний игры
        self.keys = ["available_edges"]  # принцип, по которому агент запоминает состояния
        self.type = "AGENT"  # тип игрока - агент

    def make_move(self, game):
        """
        Принимает решение о действии на основе информации о состоянии игры.
        """
        current_state = game[-1]  # текущее состояние
        if current_state["gameover"]:  # если игра уже закончена
            self.terminal_state = True  # работа агента завершена
            self.Q_learning(game, 0.0)  # пересчет Q-значения
            return None
        available_edges = current_state["available_edges"]  # доступные действия
        fl = True  # знакомо ли текущее состояние агенту
        for i, state in enumerate(self.q_states):  # поиск текущего состояния в списке знакомых агенту
            fl = True
            for str in self.keys:
                if state[str] != current_state[str]:
                    fl = False
                    break
            if fl:  # если состояние знакомо, агент находит его индекс в списке
                index = i
                break
        if not fl or not self.q_states:  # если состояние не знакомо, агент его запоминает
            self.q_states.append(current_state)
            index = len(self.q_states) - 1
        arr = rand.random_sample((len(available_edges),))  # список случайных значений в полуотрезке [0, 1)
        # словарь, ключами в котором выступают доступные действия, а значениями - их полезность
        # если полезность не была определена до этого, ей присваивается случайное значение из списка выше
        dict_actions = self.q_values.setdefault(index, {e[0]: arr[i] for i, e in enumerate(available_edges)})
        best_action = max(dict_actions.items(), key=lambda x: x[1])  # поиск действия с наибольшей полезностью
        if rand.random() < EPSILON:  # учет epsilon
            edge = random.choice(list(dict_actions))  # случайный выбор действия
        else:
            edge = best_action[0]  # выбор действия с наибольшей полезностью
        self.Q_learning(game, best_action[1])  # пересчет Q-значения для предыдущего хода
        return edge

    def Q_learning(self, game, max_qvalue):
        """
        Обновляет Q-значение для действия, сделанного на прошлом ходе агента.
        """
        current_state = game[-1]  # текущее состояние
        actions = current_state["actions"]  # список всех действий в партии до текущего хода
        scores = current_state["scores"]  # список очков на момент каждого из ходов, включая текущий
        previous_state = None  # состояние на момент предыдущего хода агента
        offset = -1  # смещение, указывающий на положение последнего хода агента
        # все состояния, исключая текущее, в обратном порядке
        buff = game[::-1][1:]
        if buff is None:  # если таких состояний нет, агент действий пока не совершал
            return
        for i, st in enumerate(buff):  # поиск предыдущего состояния, соответствующего ходу агента
            if st["current_player"] is self:  # если такое состояние найдено
                previous_state = st  # состояние найдено
                offset -= i  # установка смещения
                break
        if previous_state is None:  # если такое состояние не найдено
            return
        for i, state in enumerate(self.q_states):  # поиск текущего состояния в списке знакомых агенту
            fl = True  # найдено ли оно
            for str in self.keys:
                if state[str] != previous_state[str]:
                    fl = False
                    break
            if fl:  # если найдено
                index = i  # индекс предыдущего состояния
                break
        previous_score = scores[offset - 1]  # очки на начало предыдущего хода агента
        previous_action = actions[offset][1]  # предыдущее действие агента
        current_score = scores[-1]  # текущие очки
        players = current_score.keys()  # список игроков
        # вычисление разницы в очках между текущим и предыдущим ходом агента
        delta_score = {k: current_score[k] - previous_score[k] for k in players}
        # начиление бонусных очков за предыдущий ход
        reward = STEP_PENALTY  # штраф за очередной ход
        for p in players:
            delta = delta_score[p]  # разница в очках на текущий и предыдущий ход агента
            if p is self:
                reward += SCORE_BONUS * delta  # увеличение награды за повышение очков у агента
            else:
                reward += OPPONENT_PENALTY * delta  # уменьшение награды за повышение очков у оппонента
        win = current_state["win"]  # получение информации о победителе
        if win is not None:  # если победитель есть
            if win[0] is self:  # если победитель - агент
                reward += WIN_BONUS  # увеличение награды за победу
            else:  # если победитель - оппонент
                reward += LOSE_PENALTY  # уменьшение награды за поражение
        current_qvalue = self.q_values[index][previous_action]  # текущее Q-значение
        new_qvalue = current_qvalue + ALPHA * (reward + GAMMA * max_qvalue - current_qvalue)  # новое Q-значение
        self.q_values[index][previous_action] = new_qvalue  # обновление Q-значения
