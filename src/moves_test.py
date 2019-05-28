import unittest

from moves import move_row, move_col, is_movable_tile, move_tile, get_opposite_tile


class TestBoardMethods(unittest.TestCase):

    def test_move_row(self):
        init_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        board = move_row(init_board, 1, 0, 4, 1)
        self.assertEqual(board, expected_board)

    def test_move_row_tile_existing(self):
        init_board = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        board = move_row(init_board, 1, 0, 4, 1)
        self.assertEqual(board, expected_board)

    def test_move_row_tile_existing_end(self):
        init_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        board = move_row(init_board, 1, 4, 0, 1)
        self.assertEqual(board, expected_board)

    def test_move_col(self):
        init_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        board = move_col(init_board, 1, 0, 4, 1)
        self.assertEqual(board, expected_board)

    def test_move_col_tile_existing(self):
        init_board = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        board = move_col(init_board, 1, 0, 4, 1)
        self.assertEqual(board, expected_board)

    def test_move_col_tile_existing_end(self):
        init_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        expected_board = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        board = move_col(init_board, 1, 4, 0, 1)
        self.assertEqual(board, expected_board)

    def test_is_movable_tile(self):
        acceptable = is_movable_tile(0, 1)
        self.assertTrue(acceptable)
        unacceptable = is_movable_tile(1, 1)
        self.assertFalse(unacceptable)

    def test_move_tile(self):
        init_board = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, -1, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, -1, 0, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        tile_start = (0, 1)
        tile_end = (4, 1)
        board = move_tile(init_board, tile_start, tile_end, 1)
        self.assertEqual(board, expected_board)

    def test_get_opposite_tile(self):
        (x, y) = get_opposite_tile(0, 1)
        self.assertEqual((x, y), (4, 1))
