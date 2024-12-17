import unittest
from textwrap import dedent
from unittest.mock import patch
from io import StringIO
import p2 as p

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
      #####
      #..E#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 4)

  @patch('builtins.open')
  def test_tiny2(self, mock_open):
    mockOpen(mock_open, """
      ######
      #...E#
      #....#
      #....#
      #S#..#
      ######
    """)
    self.assertEqual(p.main(), 7)

  @patch('builtins.open')
  def test_tiny3(self, mock_open):
    mockOpen(mock_open, """
      #####
      #..E#
      #...#
      #S#.#
      #####
    """)
    self.assertEqual(p.main(), 5)

  @patch('builtins.open')
  def test_tiny4(self, mock_open):
    mockOpen(mock_open, """
      #####
      #..E#
      #.#.#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 5)

  @patch('builtins.open')
  def test_tiny55(self, mock_open):
    mockOpen(mock_open, """
      #####
      #..E#
      ###.#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 5)

  @patch('builtins.open')
  def test_tiny56(self, mock_open):
    mockOpen(mock_open, """
      #####
      ###E#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 4)

  @patch('builtins.open')
  def test_tiny6(self, mock_open):
    mockOpen(mock_open, """
      ######
      #.#.E#
      #S...#
      ######
    """)
    self.assertEqual(p.main(), 5)

  @patch('builtins.open')
  def test_tiny7(self, mock_open):
    mockOpen(mock_open, """
      ########
      #...#.E#
      #.#.#..#
      #S.....#
      ########
    """)
    self.assertEqual(p.main(), 8)

  @patch('builtins.open')
  def test_tiny8(self, mock_open):
    mockOpen(mock_open, """
      #####
      ##.E#
      #...#
      #S..#
      #####
    """)
    self.assertEqual(p.main(), 7)

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
    self.assertEqual(p.main(), 45)

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
    self.assertEqual(p.main(), 64)

if __name__ == '__main__':
  unittest.main()
