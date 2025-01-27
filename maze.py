from cell import Cell
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []
        self._create_cells()

    def _create_cells(self):
        y = self._y1
        for col in range(self._num_cols):
            x = self._x1
            _row = []
            for row in range(self._num_rows):
                cell = Cell(
                    True,
                    True,
                    True,
                    True,
                    x,
                    x + self._cell_size_x,
                    y,
                    y + self._cell_size_y,
                    self._win,
                )
                _row.append(cell)
                x += self._cell_size_x
            self._cells.append(_row)
            y += self._cell_size_y

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.01)
