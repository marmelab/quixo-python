import unittest

from board import create_board, get_symbol


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
        self.assertEqual(get_symbol(1), 'O')
        self.assertEqual(get_symbol(-1), 'X')
        self.assertEqual(get_symbol(0), ' ')
