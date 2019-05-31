import unittest
from playerio import get_symbol


class TestPlayerioMethods(unittest.TestCase):

    def test_get_symbol(self):
        self.assertEqual(get_symbol(1), 'X')
        self.assertEqual(get_symbol(-1), 'O')
        self.assertEqual(get_symbol(0), ' ')
