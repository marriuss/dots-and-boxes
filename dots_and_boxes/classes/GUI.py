import pygame
import sys
import time

from dots_and_boxes.settings.GUI_settings import *
from dots_and_boxes.settings.colors import *

class GUI:
    """
    Класс для представления GUI.
    """

    def __init__(self):
        self.exists = SHOW_GUI
        if self.exists:
            pygame.init()
            pygame.display.set_caption("Dots and Boxes")
            self.canvas = pygame.display.set_mode((WIDTH, HEIGHT + STATUS_BAR_SIZE))
            self.font = pygame.font.SysFont("comicsansms", FONT_SIZE)

    def draw_background(self):
        """
        Отрисовывает поле в начальном состоянии.
        """
        if self.exists:
            self.canvas.fill(ALICE_BLUE)

            for i in range(1, SIZE + 1):
                a = i * CELL_SIZE + (i - 1) * BORDER_SIZE + 1
                self.draw_line(BLACK, (a, 0), (a, HEIGHT), BORDER_SIZE)
                self.draw_line(BLACK, (0, a), (HEIGHT, a), BORDER_SIZE)

            self.update()

    def draw_dot(self, color, centre):
        """
        Отрисовывает точку.
        """
        if self.exists:
            pygame.draw.circle(self.canvas, color, centre, DOT_SIZE)

    def draw_line(self, color, coord1, coord2, width):
        """
        Отрисовывает линию.
        """
        if self.exists:
            pygame.draw.line(self.canvas, color, coord1, coord2, width)

    def draw_win_text(self, name, score, color):
        """
        Отрисовывает текст с информацией об исходе партии.
        """
        if self.exists:
            str = "WIN: {}   SCORE: {}".format(name, score)
            text = self.font.render(str, True, color)
            self.canvas.blit(text, ((CELLS_OFFSET + BORDER_OFFSET) // 6, CELLS_OFFSET + BORDER_OFFSET))
            self.update()

    def update(self):
        """
        Обновляет экран.
        """
        if self.exists:
            pygame.display.flip()

    def pause(self, t):
        """
        Ставит программу на паузу.
        """
        if self.exists:
            time.sleep(t)

    def exit(self):
        """
        Выход из программы.
        """
        if self.exists:
            pygame.event.pump()  # обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
