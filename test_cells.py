from main import Point, Line, Cell, Window

# Create a new window with a size of 800x600 pixels
height = 800
width = 600
win = Window(800, 600)

# Create some cells to add to the window
x_pos = 10
y_pos = 10

cells = []

for left in [True, False]:
    for right in [True, False]:
        for top in [True, False]:
            for bottom in [True, False]:

                cell = Cell(
                    left, right, top, bottom, x_pos, x_pos + 10, y_pos, y_pos + 10, win
                )
                x_pos += 20
                # Row wrapping
                if x_pos > 160:
                    x_pos = 10
                    y_pos += 60
                cells.append(cell)

undo = False
for cell_i, cell in enumerate(cells):
    cell.draw()
    cell.draw_move(cells[cell_i - 1], undo=undo)
    undo = not undo

# Run the window
win.run()
