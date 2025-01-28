# Test the maze drawing

from main import Maze, Window, Cell

win = Window(1200, 800)

n_cols = 10
n_rows = 10

maze = Maze(10, 10, n_rows, n_cols, 10, 10, win)

for col in range(n_cols):
    for row in range(n_rows):
        maze._draw_cell(col, row)

maze._break_entrance_and_exit()

maze._break_walls_r(0, 0)

win.run()
