import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1._cells[0][0].has_top_wall
        )  # Entrance is top wall of top-left cell
        self.assertFalse(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall
        )  # Exit is bottom wall of bottom-right cell

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()
        for col in range(m1._num_cols):
            for row in range(m1._num_rows):
                self.assertFalse(m1._cells[col][row].visited)


if __name__ == "__main__":
    unittest.main()
