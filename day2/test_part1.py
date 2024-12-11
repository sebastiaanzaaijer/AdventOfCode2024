import unittest

from .part1 import solve_puzzle


class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
        self.assertEqual(solve_puzzle(example_input), 2)
