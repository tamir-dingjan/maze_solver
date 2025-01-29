# Test the maze drawing

from main import Window
from maze import Maze

win = Window(1200, 800)

n_cols = 10
n_rows = 6

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

# maze._break_shared_wall(0, 0, 0, 1)

maze._draw_all_cells()

maze._break_walls_r(0, 0)

maze._reset_cells_visited()

maze.solve()

win.run()
