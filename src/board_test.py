import unittest

from board import create_board, get_symbol, is_movable_tile, get_movables_tiles, get_possibles_destinations
from constants import N_ROWS, N_COLS, INDEX_LAST_ROW, INDEX_LAST_COL


class TestBoardMethods(unittest.TestCase):

    def test_empty_board(self):
        empty_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(create_board(), empty_board)

    def test_get_symbol(self):
        self.assertEqual(get_symbol(1), 'X')
        self.assertEqual(get_symbol(-1), 'O')
        self.assertEqual(get_symbol(0), ' ')

    def test_is_movable_tile(self):
        self.assertTrue(is_movable_tile(0, 0))
        self.assertTrue(is_movable_tile(4, 4))
        self.assertTrue(is_movable_tile(0, 2))
        self.assertTrue(is_movable_tile(3, 4))
        self.assertFalse(is_movable_tile(3, 3))
        self.assertFalse(is_movable_tile(1, 1))

    def test_get_movables_tiles(self):
        empty_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_movables = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
        ]
        self.assertEqual(get_movables_tiles(empty_board), expected_movables)

    def test_get_possibles_destinations_corner(self):
        x, y = (0, 0)
        empty_board = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_destinations = [(0, 4), (4, 0)]
        destinations = get_possibles_destinations(empty_board, x, y)

        for expected_dest in expected_destinations:
            self.assertIn(expected_dest, destinations)

    def test_get_possibles_destinations_row(self):
        x, y = (0, 1)
        empty_board = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_destinations = [(0, 0), (0, 4), (4, 1)]
        destinations = get_possibles_destinations(empty_board, x, y)

        for expected_dest in expected_destinations:
            self.assertIn(expected_dest, destinations)

    def test_get_possibles_destinations_col(self):
        x, y = (1, 0)
        empty_board = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_destinations = [(0, 0), (4, 0), (1, 4)]
        destinations = get_possibles_destinations(empty_board, x, y)

        for expected_dest in expected_destinations:
            self.assertIn(expected_dest, destinations)

    def test_get_possibles_destinations_col_last(self):
        x, y = (1, 4)
        empty_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_destinations = [(0, 4), (4, 4), (1, 0)]
        destinations = get_possibles_destinations(empty_board, x, y)

        for expected_dest in expected_destinations:
            self.assertIn(expected_dest, destinations)
