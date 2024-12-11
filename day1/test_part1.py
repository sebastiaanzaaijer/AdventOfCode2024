import unittest

from .part1 import solve_puzzle


class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
        self.assertEqual(solve_puzzle(example_input), 11)
