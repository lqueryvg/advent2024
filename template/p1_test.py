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
    pass

  @patch('builtins.open')
  def test_tiny1(self, mock_open):
    mockOpen(mock_open, """
             0 1 10 99 999
    """)
    self.assertEqual(p.main(), 999)
    # self.assertEqual(p.someGlobal, ['1', '2024', '1', '9', '2021976', '0', '9'])

  @patch('builtins.open')
  def xtest_example1(self, mock_open):
    mockOpen(mock_open, """
             0 1 10 99 999
    """)
    # mockOpen(mock_open, "125 17")
    self.assertEqual(p.main(), 999)

if __name__ == '__main__':
  unittest.main()
