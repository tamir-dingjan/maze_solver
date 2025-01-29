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
        x = self._x1
        for col in range(self._num_cols):
            y = self._y1
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
                y += self._cell_size_y
            self._cells.append(_row)
            x += self._cell_size_x

    def _draw_all_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

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
            rows.append(j)
        if i < self._num_cols - 1:
            cols.append(i + 1)
            rows.append(j)
        if j > 0:
            cols.append(i)
            rows.append(j - 1)
        if j < self._num_rows - 1:
            cols.append(i)
            rows.append(j + 1)

        return list(zip(cols, rows))

    def _break_shared_wall(self, i1, j1, i2, j2):
        """
        Break the shared wall between the two cells located at (i1, j1) and (i2, j2).
        """
        if (i1 == i2) and (j1 == j2):
            raise ValueError("Cells are the same!")

        # Check the provided cell indices are adjacent
        if not (i2, j2) in self._get_adjacent_cells(i1, j1):
            raise ValueError("Cells are not adjacent!")

        if i1 < i2:
            # Break to the right of cell 1
            self._cells[i1][j1].has_right_wall = False
            self._cells[i2][j2].has_left_wall = False
        elif i1 > i2:
            # Break to the left of cell 1
            self._cells[i1][j1].has_left_wall = False
            self._cells[i2][j2].has_right_wall = False
        elif j1 < j2:
            # Break below cell 1
            self._cells[i1][j1].has_bottom_wall = False
            self._cells[i2][j2].has_top_wall = False
        elif j1 > j2:
            # Break above cell 1
            self._cells[i1][j1].has_top_wall = False
            self._cells[i2][j2].has_bottom_wall = False

    def _break_walls_r(self, i, j):
        # TODO: This doesn't yet create a path from the entrance to the exit

        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check if adjacent cells have not yet been visited
            for col, row in self._get_adjacent_cells(i, j):
                if self._cells[col][row].visited:
                    # print("This cell has already been visited! Skipping.")
                    continue
                else:
                    to_visit.append((col, row))
            # If there are no unvisited adjacent cells, we draw the current cell and return
            # print(f"No. of cells to visit: {len(to_visit)}")
            if to_visit == []:
                self._draw_cell(i, j)
                # print("All this cell's neighbours have been visited! Returning.")
                return
            # Otherwise, we choose a random unvisited adjacent cell and break the wall between them
            col, row = random.choice(to_visit)

            self._break_shared_wall(i, j, col, row)

            self._break_walls_r(col, row)

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False

    def _is_blocking_wall(self, i1, j1, i2, j2):
        """
        Checks if the cell at self._cells[i1][j1] has a wall blocking the path to self._cells[i2][j2].
        """
        if (i1 == i2) and (j1 == j2):
            raise ValueError("Cells are the same!")

        # Check the provided cell indices are adjacent
        if not (i2, j2) in self._get_adjacent_cells(i1, j1):
            raise ValueError("Cells are not adjacent!")

        if i1 < i2:
            return (
                self._cells[i1][j1].has_right_wall or self._cells[i2][j2].has_left_wall
            )
        elif i1 > i2:
            return (
                self._cells[i1][j1].has_left_wall or self._cells[i2][j2].has_right_wall
            )
        elif j1 < j2:
            return (
                self._cells[i1][j1].has_bottom_wall or self._cells[i2][j2].has_top_wall
            )
        elif j1 > j2:
            return (
                self._cells[i1][j1].has_top_wall or self._cells[i2][j2].has_bottom_wall
            )

        return False

    def solve(self):
        solved = self._solve_r(0, 0)
        if solved:
            return True
        else:
            return False

    def _solve_r(self, x, y):
        self._animate()
        self._cells[x][y].visited = True

        # print(f"Current cell: {self._cells[x][y]}")

        # If we are at the end of the maze, return True
        if x == self._num_cols - 1 and y == self._num_rows - 1:
            return True

        # Get adjacent cells
        adj_cells = self._get_adjacent_cells(x, y)
        for adj_col, adj_row in adj_cells:

            print(
                f"\tAdjacent cell: {adj_col,adj_row}, visited: {self._cells[adj_col][adj_row].visited}, blocking wall: {self._is_blocking_wall(x,y,adj_col,adj_row)}"
            )

            # Only visit a cell if it hasn't been visited, and there's no blocking walls between the current cell and the adjacent cell
            if (not self._cells[adj_col][adj_row].visited) and (
                not self._is_blocking_wall(x, y, adj_col, adj_row)
            ):
                print(f"Moving to adjacent cell: {adj_col,adj_row}")
                # Draw a move from the current cell to the adjacent cell
                self._cells[x][y].draw_move(self._cells[adj_col][adj_row])
                # If the next cell is the end of the maze, return True
                if self._solve_r(adj_col, adj_row) == True:
                    return True
                # Otherwise, draw an "undo" move from the adjacent cell back to the current cell
                print(f"\tUndoing move from the adjacent cell: {adj_col,adj_row}")
                self._cells[adj_col][adj_row].draw_move(self._cells[x][y], undo=True)
                self._animate()
        # If no valid path is found, return False
        return False
