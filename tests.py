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

    def test_adjacent_cell_detection_true_neighbours(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Every pair of cells which differs by either a single row or column should be adjacent
        for col in range(1, num_cols):
            for row in range(1, num_rows):
                nbors = []

                if col > 0:
                    nbors.append((col - 1, row))
                if col < num_cols - 1:
                    nbors.append((col + 1, row))
                if row > 0:
                    nbors.append((col, row - 1))
                if row < num_rows - 1:
                    nbors.append((col, row + 1))

                # Check that every neighbour is detected as adjacent
                for nbor in nbors:
                    self.assertTrue(nbor in m1._get_adjacent_cells(col, row))

                # Check that every detected adjacent cell is a true neighbour
                for detected_adjacent_cell in m1._get_adjacent_cells(col, row):
                    self.assertTrue(detected_adjacent_cell in nbors)

    def test_break_shared_wall_single(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Break a shared wall between the cells at 0,0 and 0,1
        # This is the bottom wall of cell1, and the top wall of cell2
        m1._break_shared_wall(0, 0, 0, 1)
        self.assertFalse(m1._cells[0][0].has_bottom_wall)
        self.assertFalse(m1._cells[0][1].has_top_wall)

    def test_break_shared_wall_all(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Break all the shared walls
        for i1 in range(num_cols):
            for j1 in range(num_rows):
                nbors = m1._get_adjacent_cells(i1, j1)
                for i2, j2 in nbors:
                    m1._break_shared_wall(i1, j1, i2, j2)

                    if i1 < i2:
                        # Test break to the right of cell 1
                        self.assertFalse(m1._cells[i1][j1].has_right_wall)
                        self.assertFalse(m1._cells[i2][j2].has_left_wall)
                    elif i1 > i2:
                        # Test break to the left of cell 1
                        self.assertFalse(m1._cells[i1][j1].has_left_wall)
                        self.assertFalse(m1._cells[i2][j2].has_right_wall)
                    elif j1 < j2:
                        # Test break below cell 1
                        self.assertFalse(m1._cells[i1][j1].has_bottom_wall)
                        self.assertFalse(m1._cells[i2][j2].has_top_wall)
                    elif j1 > j2:
                        # Break above cell 1
                        self.assertFalse(m1._cells[i1][j1].has_top_wall)
                        self.assertFalse(m1._cells[i2][j2].has_bottom_wall)

    def test_blocking_wall_detection(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=0)
        # All walls present, every cell should be blocked from its neighbours
        self.assertTrue(m1._cells[0][0].has_bottom_wall)
        self.assertTrue(m1._cells[0][1].has_top_wall)
        self.assertTrue(m1._is_blocking_wall(0, 0, 0, 1))
        self.assertTrue(m1._is_blocking_wall(0, 1, 0, 0))

        for col in range(m1._num_cols):
            for row in range(m1._num_rows):
                # print(f"Current cell: {col,row}")
                for adj_col, adj_row in m1._get_adjacent_cells(col, row):
                    # print(f"\tAdjacent cell: {adj_col,adj_row}")
                    self.assertTrue(m1._is_blocking_wall(col, row, adj_col, adj_row))

        m1._break_shared_wall(2, 4, 1, 4)
        self.assertFalse(m1._is_blocking_wall(2, 4, 1, 4))


if __name__ == "__main__":
    unittest.main()
