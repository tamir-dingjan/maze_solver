from tkinter import Tk, BOTH, Canvas


class Window(Tk):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.geometry(f"{width}x{height}")

        self.canvas = Canvas(master=self.root, bg="white")
        self.canvas.pack()

        self.running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close())

        self.root.mainloop()

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw

    def close(self):
        self.running = False


# Create the main window
win = Window(800, 600)
win.wait_for_close()
