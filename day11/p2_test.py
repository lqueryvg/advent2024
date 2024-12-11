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
    p.cache = {}

  @patch('builtins.open')
  def test_teeny(self, mock_open):
    mockOpen(mock_open, "0")
    self.assertEqual(p.main(1), 1)
    self.assertEqual(p.cache, {('1', 0): 1})

  @patch('builtins.open')
  def test_teeny2(self, mock_open):
    mockOpen(mock_open, "0")
    self.assertEqual(p.main(2), 1)
    self.assertEqual(p.cache, {('2024', 0): 1, ('1', 1): 1})

  @patch('builtins.open')
  def test_teeny3(self, mock_open):
    mockOpen(mock_open, "0")
    self.assertEqual(p.main(3), 2)

  @patch('builtins.open')
  def test_tiny1(self, mock_open):
    mockOpen(mock_open, "0 1 10 99 999")
    self.assertEqual(p.main(1), 7)

  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, "125 17")
    self.assertEqual(p.main(6), 22)
    p.stones = []
    mockOpen(mock_open, "125 17")
    self.assertEqual(p.main(25), 55312)

if __name__ == '__main__':
  unittest.main()
