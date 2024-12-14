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

  def test_calc(self):
    self.assertEqual(p.move(2, 2, 0, 11), 2)
    self.assertEqual(p.move(2, 2, 1, 11), 4)
    self.assertEqual(p.move(2, 2, 2, 11), 6)
    self.assertEqual(p.move(2, 2, 3, 11), 8)
    self.assertEqual(p.move(2, 2, 4, 11), 10)
    self.assertEqual(p.move(2, 2, 5, 11), 1)

    self.assertEqual(p.move(4, -3, 0, 7), 4)
    self.assertEqual(p.move(4, -3, 1, 7), 1)
    self.assertEqual(p.move(4, -3, 2, 7), 5)
    self.assertEqual(p.move(4, -3, 3, 7), 2)
    self.assertEqual(p.move(4, -3, 4, 7), 6)
    self.assertEqual(p.move(4, -3, 5, 7), 3)
    # self.assertEqual(p.someGloba5, ['1', '2024', '1', '9', '2021976', '0', '9'])

  @patch('builtins.open')
  def xtest_example1(self, mock_open):
    mockOpen(mock_open, """
             0 1 10 99 999
    """)
    # mockOpen(mock_open, "125 17")
    self.assertEqual(p.main(), 999)

if __name__ == '__main__':
  unittest.main()
