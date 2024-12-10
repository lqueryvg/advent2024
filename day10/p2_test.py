import unittest
from textwrap import dedent
from unittest.mock import patch
from io import StringIO
import day10.p2 as p2

def getMockFile(s):
  return StringIO(dedent(s).lstrip())

def mockOpen(mock_open, s):
  mock_file = getMockFile(s)
  mock_open.return_value.__enter__.return_value = mock_file


class TestP2(unittest.TestCase):

  def setUp(self):
    p2.reachables = set()
    p2.TARGET_VALUE = 9


  @patch('builtins.open')
  def test_tiny1(self, mock_open):
    mockOpen(mock_open, """
      01
      12
    """)

    p2.TARGET_VALUE = 2
    self.assertEqual(p2.main(), 2)
    # p2.main()

    self.assertEqual(p2.reachables, {((0, 0), (1, 1))})
    self.assertEqual(p2.start, (0, 0))

  @patch('builtins.open')
  def test_tiny2(self, mock_open):
    mockOpen(mock_open, """
      01.
      .2.
      .34
    """)
    p2.TARGET_VALUE = 4
    self.assertEqual(p2.main(), 1)

  @patch('builtins.open')
  def test_tiny3(self, mock_open):
    mockOpen(mock_open, """
      012
      113
      111
    """)
    p2.TARGET_VALUE = 3
    self.assertEqual(p2.main(), 1)

  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, """
      .....0.
      ..4321.
      ..5..2.
      ..6543.
      ..7..4.
      ..8765.
      ..9....    
    """)
    self.assertEqual(p2.main(), 3)

  @patch('builtins.open')
  def test_example2(self, mock_open):
    mockOpen(mock_open, """
      ..90..9
      ...1.98
      ...2..7
      6543456
      765.987
      876....
      987....
    """)
    self.assertEqual(p2.main(), 13)

  @patch('builtins.open')
  def test_example3(self, mock_open):
    mockOpen(mock_open, """
      012345
      123456
      234567
      345678
      4.6789
      56789.
    """)
    self.assertEqual(p2.main(), 227)

  @patch('builtins.open')
  def test_full_example(self, mock_open):
    mockOpen(mock_open, """
      89010123
      78121874
      87430965
      96549874
      45678903
      32019012
      01329801
      10456732
    """)
    self.assertEqual(p2.main(), 81)

if __name__ == '__main__':
  unittest.main()