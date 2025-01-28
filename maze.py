from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self.seed = random.seed(seed)

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
        if self._win != None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.01)

    def _break_entrance_and_exit(self):
        # Entrance is always the top wall of the top-left cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        # Exit is always at the bottom of the bottom-right cell
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _get_adjacent_cells(self, i, j):
        # Get all adjacent cells that are within the maze boundaries
        cols = []
        rows = []

        if i > 0:
            cols.append(i - 1)
            cols.append(j)
        if i < self._num_rows - 1:
            cols.append(i + 1)
            rows.append(j)
        if j > 0:
            cols.append(i)
            rows.append(j - 1)
        if j < self._num_cols - 1:
            cols.append(i)
            rows.append(j + 1)

        return list(zip(rows, cols))

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            # Check if adjacent cells have not yet been visited
            for adjacent in self._get_adjacent_cells(i, j):
                row, col = adjacent
                if self._cells[row][col].visited:
                    continue
                to_visit.append((row, col))
            # If there are no unvisited adjacent cells, we draw the current cell and return
            if to_visit == []:
                self._draw_cell(i, j)
                return
            # Otherwise, we choose a random unvisited adjacent cell and break the wall between them
            row, col = random.choice(to_visit)

            # Choose the wall to break by the direction of the chosen adjacent cell
            if row > j:
                current_cell.has_bottom_wall = False
                self._cells[row][col].has_top_wall = False
            elif row < j:
                current_cell.has_top_wall = False
                self._cells[row][col].has_bottom_wall = False
            elif col > i:
                current_cell.has_right_wall = False
                self._cells[row][col].has_left_wall = False
            elif col < i:
                current_cell.has_left_wall = False
                self._cells[row][col].has_right_wall = False

            self._break_walls_r(row, col)

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False
