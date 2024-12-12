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
    p.visited = set()
    p.pathsSeen = set()
    p.grid = []

  @patch('builtins.open')
  def test_tiny_A(self, mock_open):
    mockOpen(mock_open, "A")
    self.assertEqual(p.main(), 4)

  @patch('builtins.open')
  def test_tiny_AA(self, mock_open):
    mockOpen(mock_open, "AA")
    self.assertEqual(p.main(), 8)

  @patch('builtins.open')
  def test_tiny_AAB(self, mock_open):
    mockOpen(mock_open, "AAB")
    self.assertEqual(p.main(), 12)

  @patch('builtins.open')
  def test_tiny_AAAB(self, mock_open):
    mockOpen(mock_open, """
      AA
      AB
    """)
    self.assertEqual(p.main(), 22)

  @patch('builtins.open')
  def test_example3_e_shape(self, mock_open):
    mockOpen(mock_open, """
      EEEEE
      EXXXX
      EEEEE
      EXXXX
      EEEEE
    """)
    self.assertEqual(p.main(), 236)

  @patch('builtins.open')
  def test_tiny_ABC(self, mock_open):
    mockOpen(mock_open, """
      AAA
      BBC
      BBC
    """)
    self.assertEqual(p.main(), 36)
  
  @patch('builtins.open')
  def test_tiny_ABCE(self, mock_open):
    mockOpen(mock_open, """
      AAA
      BBC
      BBC
      EEE
    """)
    self.assertEqual(p.main(), 48)

  @patch('builtins.open')
  def test_tiny_AAAA(self, mock_open):
    mockOpen(mock_open, """
      AA
      AA
    """)
    self.assertEqual(p.main(), 16)
  
  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, """
      AAAA
      BBCD
      BBCC
      EEEC
    """)
    self.assertEqual(p.main(), 80)

  @patch('builtins.open')
  def test_tiny_OXO_1(self, mock_open):
    mockOpen(mock_open, """
      OOO
      OXO
    """)
    self.assertEqual(p.main(), 44)

  @patch('builtins.open')
  def test_tiny_OXO_2(self, mock_open):
    mockOpen(mock_open, """
      OO
      OX
      OO
    """)
    self.assertEqual(p.main(), 44)

  @patch('builtins.open')
  def test_tiny_OXO_3(self, mock_open):
    mockOpen(mock_open, """
      OO
      XO
      OO
    """)
    self.assertEqual(p.main(), 44)

  @patch('builtins.open')
  def test_tiny_OXO_4(self, mock_open):
    mockOpen(mock_open, """
      OO
      XO
      XO
      OO
    """)
    self.assertEqual(p.main(), 56)

  @patch('builtins.open')
  def test_tiny_OXO(self, mock_open):
    mockOpen(mock_open, """
      OOO
      OXO
      OOO
    """)
    self.assertEqual(p.main(), 68)

  @patch('builtins.open')
  def test_example2(self, mock_open):
    mockOpen(mock_open, """
      OOOOO
      OXOXO
      OOOOO
      OXOXO
      OOOOO
    """)
    self.assertEqual(p.main(), 436)

  @patch('builtins.open')
  def test_example4_AB(self, mock_open):
    mockOpen(mock_open, """
      AAAAAA
      AAABBA
      AAABBA
      ABBAAA
      ABBAAA
      AAAAAA
    """)
    self.assertEqual(p.main(), 368)

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
    self.assertEqual(p.main(), 1206)

if __name__ == '__main__':
  unittest.main()
