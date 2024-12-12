import unittest
from textwrap import dedent
from unittest.mock import patch
from io import StringIO
import p1 as p

def getMockFile(s):
  return StringIO(dedent(s).lstrip())

def mockOpen(mock_open, s):
  mock_file = getMockFile(s)
  mock_open.return_value.__enter__.return_value = mock_file

class Test(unittest.TestCase):

  def setUp(self):
    # set globals up here
    #p.someGlobal = someValue
    p.visited = set()
    p.grid = []

  @patch('builtins.open')
  def test_tiny_A(self, mock_open):
    mockOpen(mock_open, "A")
    self.assertEqual(p.main(), 4)

  @patch('builtins.open')
  def test_tiny_AA(self, mock_open):
    mockOpen(mock_open, "AA")
    self.assertEqual(p.main(), 12)

  @patch('builtins.open')
  def test_tiny_AB(self, mock_open):
    mockOpen(mock_open, "AB")
    self.assertEqual(p.main(), 8)

  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, """
      AAAA
      BBCD
      BBCC
      EEEC
    """)
    self.assertEqual(p.main(), 140)
    # self.assertEqual(p.someGlobal, ['1', '2024', '1', '9', '2021976', '0', '9'])

  @patch('builtins.open')
  def test_example_OXO(self, mock_open):
    mockOpen(mock_open, """
      OOOOO
      OXOXO
      OOOOO
      OXOXO
      OOOOO
    """)
    self.assertEqual(p.main(), 772)

  @patch('builtins.open')
  def test_tiny_OXO(self, mock_open):
    mockOpen(mock_open, """
      OOO
      OXO
      OOO
    """)
    self.assertEqual(p.main(), 132)

  @patch('builtins.open')
  def test_example_large(self, mock_open):
    mockOpen(mock_open, """
      RRRRIICCFF
      RRRRIICCCF
      VVRRRCCFFF
      VVRCCCJFFF
      VVVVCJJCFE
      VVIVCCJJEE
      VVIIICJJEE
      MIIIIIJJEE
      MIIISIJEEE
      MMMISSJEEE
    """)
    self.assertEqual(p.main(), 1930)

if __name__ == '__main__':
  unittest.main()
