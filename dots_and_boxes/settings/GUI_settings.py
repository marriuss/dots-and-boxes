from .game import SIZE

SHOW_GUI = True
CELL_SIZE = 50
BORDER_SIZE = 1
DOT_SIZE = CELL_SIZE // 6
FONT_SIZE = CELL_SIZE // 3
STATUS_BAR_SIZE = FONT_SIZE * 2 + 5
CELLS_OFFSET = SIZE * CELL_SIZE
BORDER_OFFSET = SIZE * BORDER_SIZE
CENTRE = CELL_SIZE + BORDER_SIZE

FONT_NAME = "papyrus"

WIDTH = SIZE * CELL_SIZE + (SIZE - 1) * BORDER_SIZE
HEIGHT = SIZE * CELL_SIZE + (SIZE - 1) * BORDER_SIZE

STEP_PAUSE = 0.2
EPISODE_PAUSE = 0.5
