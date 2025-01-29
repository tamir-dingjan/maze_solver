from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line
from cell import Cell
from maze import Maze


class Window(Tk):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.title("Maze Solver")
        self.geometry(f"{width}x{height}")

        # Create a canvas to draw on
        self.canvas = Canvas(master=self, width=width, height=height, bg="white")
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

    win = Window(1200, 800)

    n_cols = 50
    n_rows = 30

    maze = Maze(
        x1=50,
        y1=50,
        num_rows=n_rows,
        num_cols=n_cols,
        cell_size_x=20,
        cell_size_y=20,
        win=win,
        seed=0,
    )

    maze._draw_all_cells()

    maze._break_entrance_and_exit()

    maze._break_walls_r(0, 0)

    maze._reset_cells_visited()

    maze.solve()

    win.run()
