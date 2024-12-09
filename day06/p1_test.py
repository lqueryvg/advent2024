import unittest

from day06.p1 import turn

class TestTurn(unittest.TestCase):
  def test_turn_from_north(self):
    self.assertEqual(turn([0, -1]), [1, 0])
    self.assertEqual(turn([0, 1]), [-1, 0])

  def test_turn_from_west(self):
    self.assertEqual(turn([-1, 0]), [0, -1])
    self.assertEqual(turn([1, 0]), [0, 1])


if __name__ == '__main__':
    unittest.main()
