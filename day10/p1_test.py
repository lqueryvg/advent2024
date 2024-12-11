import unittest
from textwrap import dedent
from unittest.mock import patch
from io import StringIO
import p1

def getMockFile(s):
  return StringIO(dedent(s).lstrip())

def mockOpen(mock_open, s):
  mock_file = getMockFile(s)
  mock_open.return_value.__enter__.return_value = mock_file


class TestP1(unittest.TestCase):

  def setUp(self):
    p1.reachables = set()
    p1.TARGET_VALUE = 9


  @patch('builtins.open')
  def test_tiny1(self, mock_open):
    mockOpen(mock_open, """
      01
      12
    """)

    p1.TARGET_VALUE = 2
    p1.main()

    self.assertEqual(p1.reachables, {((0, 0), (1, 1))})
    self.assertEqual(p1.start, (0, 0))

  @patch('builtins.open')
  def test_tiny2(self, mock_open):
    mockOpen(mock_open, """
      01.
      .2.
      .34
    """)
    p1.TARGET_VALUE = 4
    self.assertEqual(p1.main(), 1)

  @patch('builtins.open')
  def test_tiny3(self, mock_open):
    mockOpen(mock_open, """
      012
      113
      111
    """)
    p1.TARGET_VALUE = 3
    self.assertEqual(p1.main(), 1)

  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, """
      0123
      1234
      8765
      9876
    """)
    self.assertEqual(p1.main(), 1)

  @patch('builtins.open')
  def test_example2(self, mock_open):
    mockOpen(mock_open, """
      ...0...
      ...1...
      ...2...
      6543456
      7.....7
      8.....8
      9.....9
    """)
    self.assertEqual(p1.main(), 2)

  @patch('builtins.open')
  def test_example3(self, mock_open):
    mockOpen(mock_open, """
      10..9..
      2...8..
      3...7..
      4567654
      ...8..3
      ...9..2
      .....01
    """)
    self.assertEqual(p1.main(), 3)

  @patch('builtins.open')
  def test_example4(self, mock_open):
    mockOpen(mock_open, """
      ..90..9
      ...1.98
      ...2..7
      6543456
      765.987
      876....
      987....
    """)
    self.assertEqual(p1.main(), 4)

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
    self.assertEqual(p1.main(), 36)

if __name__ == '__main__':
  unittest.main()
