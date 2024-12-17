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
    p.a = 0
    p.b = 0
    p.c = 0

  @patch('builtins.open')
  def test_tiny_example1(self, mock_open):
    # If register C contains 9, the program 2,6 would set register B to 1.
    mockOpen(mock_open, """
      Register A: 0
      Register B: 0
      Register C: 9

      Program: 2,6
    """)
    self.assertEqual(p.main(), "")
    self.assertEqual(p.a, 0)
    self.assertEqual(p.b, 1)
    self.assertEqual(p.c, 9)

  @patch('builtins.open')
  def test_tiny_example2(self, mock_open):
    # If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
    mockOpen(mock_open, """
      Register A: 10
      Register B: 0
      Register C: 0

      Program: 5,0,5,1,5,4
    """)
    self.assertEqual(p.main(), "0,1,2")

  @patch('builtins.open')
  def test_tiny_example3(self, mock_open):
    # If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
    mockOpen(mock_open, """
      Register A: 2024
      Register B: 0
      Register C: 0

      Program: 0,1,5,4,3,0
    """)
    self.assertEqual(p.main(), "4,2,5,6,7,7,7,7,3,1,0")
    self.assertEqual(p.a, 0)

  @patch('builtins.open')
  def test_tiny_example4(self, mock_open):
    # If register B contains 29, the program 1,7 would set register B to 26.
    mockOpen(mock_open, """
      Register A: 0
      Register B: 29
      Register C: 0

      Program: 1,7
    """)
    self.assertEqual(p.main(), "")
    self.assertEqual(p.b, 26)

  @patch('builtins.open')
  def test_tiny_example5(self, mock_open):
    # If register B contains 2024 and register C contains 43690,
    # the program 4,0 would set register B to 44354.
    mockOpen(mock_open, """
      Register A: 0
      Register B: 2024
      Register C: 43690

      Program: 4,0
    """)
    self.assertEqual(p.main(), "")
    self.assertEqual(p.b, 44354)

  @patch('builtins.open')
  def test_example1(self, mock_open):
    mockOpen(mock_open, """
      Register A: 729
      Register B: 0
      Register C: 0

      Program: 0,1,5,4,3,0
    """)
    self.assertEqual(p.main(), "4,6,3,5,6,3,5,2,1,0")

if __name__ == '__main__':
  unittest.main()
