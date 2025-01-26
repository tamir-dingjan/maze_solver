from tkinter import Tk, BOTH, Canvas


class Point:
    """
    Stores the X and Y values that identify a point on the screen.

    X=0 is the left of the screen.
    Y=0 is the top of the screen.

    Attributes:
        x (int): The horizontal coordinate of the point.
        y (int): The vertical coordinate of the point.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_colour: str):
        canvas.create_line(
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y,
            fill=fill_colour,
            width=2,
        )


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
        _win,
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

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill="black"
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill="black"
            )
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill="black"
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill="black"
            )


class Window(Tk):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.title("Maze Solver")
        self.geometry(f"{width}x{height}")

        # Create a canvas to draw on
        self.canvas = Canvas(master=self, bg="white")
        self.canvas.pack()

        self.running = False

        self.protocol("WM_DELETE_WINDOW", self.close())

    def run(self):
        self.mainloop()

    def redraw(self):
        self.update_idletasks()
        self.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_colour: str):
        line.draw(self.canvas, fill_colour)


if __name__ == "__main__":
    win = Window(800, 600)

    win.draw_line(Line(Point(800, 600), Point(200, 33)), "orange")

    win.run()
