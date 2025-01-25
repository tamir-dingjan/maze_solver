from tkinter import Tk, BOTH, Canvas


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


if __name__ == "__main__":
    win = Window(800, 600)
    win.run()
