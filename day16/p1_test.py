import unittest
from textwrap import dedent
from unittest.mock import patch
from io import StringIO
import math
import p1 as p

def getMockFile(s):
  return StringIO(dedent(s).lstrip())

def mockOpen(mock_open, s):
  mock_file = getMockFile(s)
  mock_open.return_value.__enter__.return_value = mock_file

class Test(unittest.TestCase):

  def setUp(self):
    # set globals up here
    p.grid = []

  @patch('builtins.open')
  def test_tiny1(self, mock_open):
    mockOpen(mock_open, """
      ####
      #SE#
      ####
    """)
    self.assertEqual(p.main(), 2001)

  @patch('builtins.open')
  def test_tiny2(self, mock_open):
    mockOpen(mock_open, """
      #####
      #..E#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 2003)

  @patch('builtins.open')
  def test_tiny3(self, mock_open):
    mockOpen(mock_open, """
      ######
      #...E#
      #....#
      #....#
      #S#..#
      ######
    """)
    self.assertEqual(p.main(), 2006)

  @patch('builtins.open')
  def test_tiny4(self, mock_open):
    mockOpen(mock_open, """
      #####
      #..E#
      #...#
      #S#.#
      #####
    """)
    self.assertEqual(p.main(), 2004)

  @patch('builtins.open')
  def test_tiny5(self, mock_open):
    mockOpen(mock_open, """
      #####
      #..E#
      #.#.#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 2004)

  @patch('builtins.open')
  def test_tiny55(self, mock_open):
    mockOpen(mock_open, """
      #####
      #..E#
      ###.#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 3004)

  @patch('builtins.open')
  def test_tiny56(self, mock_open):
    mockOpen(mock_open, """
      #####
      ###E#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 3003)

  @patch('builtins.open')
  def test_tiny6(self, mock_open):
    mockOpen(mock_open, """
      ######
      #.#.E#
      #S...#
      ######
    """)
    self.assertEqual(p.main(), 3004)

  @patch('builtins.open')
  def test_tiny7(self, mock_open):
    mockOpen(mock_open, """
      ########
      #...#.E#
      #.#.#..#
      #S.....#
      ########
    """)
    self.assertEqual(p.main(), 3007)

  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, """
      ###############
      #.......#....E#
      #.#.###.#.###.#
      #.....#.#...#.#
      #.###.#####.#.#
      #.#.#.......#.#
      #.#.#####.###.#
      #...........#.#
      ###.#.#####.#.#
      #...#.....#.#.#
      #.#.#.###.#.#.#
      #.....#...#.#.#
      #.###.#.#.#.#.#
      #S..#.....#...#
      ###############
    """)
    self.assertEqual(p.main(), 7036)

  @patch('builtins.open')
  def test_example2(self, mock_open):
    mockOpen(mock_open, """
      #################
      #...#...#...#..E#
      #.#.#.#.#.#.#.#.#
      #.#.#.#...#...#.#
      #.#.#.#.###.#.#.#
      #...#.#.#.....#.#
      #.#.#.#.#.#####.#
      #.#...#.#.#.....#
      #.#.#####.#.###.#
      #.#.#.......#...#
      #.#.###.#####.###
      #.#.#...#.....#.#
      #.#.#.#####.###.#
      #.#.#.........#.#
      #.#.#.#########.#
      #S#.............#
      #################
    """)
    self.assertEqual(p.main(), 11048)

if __name__ == '__main__':
  unittest.main()
