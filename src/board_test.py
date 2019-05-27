import unittest

from board import create_board

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