from point import Point
from line import Line


class Cell:
    """
    Each box in the maze grid is a "Cell", which tracks if it has a wall
    on each of the four sides.

    The _x1, _x2, _y1, and _y2 attributes store the cell location on the
    canvas:
     - _x1 = left bound
     - _x2 = right bound
     - _y1 = top bound
     - _y2 = bottom bound

    The _win attribute gives access to the window so that the
    cell can draw itself.
    """

    def __init__(
        self,
        has_left_wall: bool,
        has_right_wall: bool,
        has_top_wall: bool,
        has_bottom_wall: bool,
        _x1: int,
        _x2: int,
        _y1: int,
        _y2: int,
        _win=None,
        visited=False,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win
        self.visited = visited

    def __repr__(self):
        _walls = []
        if self.has_left_wall:
            _walls.append("left")
        if self.has_right_wall:
            _walls.append("right")
        if self.has_top_wall:
            _walls.append("top")
        if self.has_bottom_wall:
            _walls.append("bottom")
        _walls = ", ".join(_walls)
        return f"Cell(walls:{_walls}, coords: x1={self._x1}, x2={self._x2}, y1={self._y1}, y2={self._y2})"

    def draw(self):

        for _wall, _line in zip(
            [
                self.has_left_wall,
                self.has_right_wall,
                self.has_top_wall,
                self.has_bottom_wall,
            ],
            [
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
            ],
        ):

            if _wall:
                fill_colour = "black"
            else:
                fill_colour = "white"

            self._win.draw_line(
                _line,
                fill_colour=fill_colour,
            )

    def draw_move(self, to_cell, undo=False):
        if undo:
            colour = "red"
        else:
            colour = "gray"

        # The line begins in the center of this cell, and ends at the center of the target cell.
        start_x = ((self._x2 - self._x1) / 2) + self._x1
        start_y = ((self._y2 - self._y1) / 2) + self._y1
        end_x = ((to_cell._x2 - to_cell._x1) / 2) + to_cell._x1
        end_y = ((to_cell._y2 - to_cell._y1) / 2) + to_cell._y1
        # Draw the line between the two cells.
        self._win.draw_line(
            Line(Point(start_x, start_y), Point(end_x, end_y)),
            fill_colour=colour,
        )
