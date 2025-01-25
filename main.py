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
