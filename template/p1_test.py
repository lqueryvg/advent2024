import unittest
from textwrap import dedent
from unittest.mock import patch
from io import StringIO
import day11.p1 as p

def getMockFile(s):
  return StringIO(dedent(s).lstrip())

def mockOpen(mock_open, s):
  mock_file = getMockFile(s)
  mock_open.return_value.__enter__.return_value = mock_file


class Test(unittest.TestCase):

  def setUp(self):
    # set globals up here
    # p.someGlobal = value
    pass

  @patch('builtins.open')
  def test_tiny1(self, mock_open):
    mockOpen(mock_open, """
      test data here
      test data here
    """)

    self.assertEqual(p.main(), 1000)
    # self.assertEqual(p.some_global, {((0, 0), (1, 1))})
    # self.assertEqual(p.start, (0, 0))

  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, """
      test data here
      test data here
    """)
    self.assertEqual(p.main(), 1000)

  @patch('builtins.open')
  def test_full_example(self, mock_open):
    mockOpen(mock_open, """
      test data here
      test data here
    """)
    self.assertEqual(p.main(), 1000)

if __name__ == '__main__':
  unittest.main()