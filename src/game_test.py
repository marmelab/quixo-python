import unittest

from game import check_success


class TestGameMethods(unittest.TestCase):

    def test_check_success_fail(self):
        board = [
            [0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0]
        ]
        self.assertFalse(check_success(board))

    def test_check_success_player_1(self):
        board = [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(check_success(board), 1)

        board = [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]
        ]
        self.assertEqual(check_success(board), 1)

        board = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ]
        self.assertEqual(check_success(board), 1)

        board = [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0]
        ]
        self.assertEqual(check_success(board), 1)

    def test_check_success_player_2(self):
        board = [
            [0, 0, 0, 0, 0],
            [-1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(check_success(board), -1)

        board = [
            [-1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0]
        ]
        self.assertEqual(check_success(board), -1)

        board = [
            [-1, 0, 0, 0, 0],
            [0, -1, 0, 0, 0],
            [0, 0, -1, 0, 0],
            [0, 0, 0, -1, 0],
            [0, 0, 0, 0, -1]
        ]
        self.assertEqual(check_success(board), -1)

        board = [
            [0, 0, 0, 0, -1],
            [0, 0, 0, -1, 0],
            [0, 0, -1, 0, 0],
            [0, -1, 0, 0, 0],
            [-1, 0, 0, 0, 0]
        ]
        self.assertEqual(check_success(board), -1)
