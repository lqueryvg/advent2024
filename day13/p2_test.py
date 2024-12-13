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
    #p.someGlobal = someValue
    pass

  def test_calculate_machine1(self):
    self.assertEqual(p.calculate(8400, 5400,	94,	34,	22,	67), 0)

  def test_calculate_machine2(self):
    self.assertEqual(p.calculate(12748, 12176, 26, 66, 67, 21), 459236326669.0)

  def test_calculate_machine3(self):
    self.assertEqual(p.calculate(7870, 6450, 17, 86,84, 37), 0)

  def test_calculate_machine4(self):
    self.assertEqual(p.calculate(18641, 10279, 69, 23, 27, 71), 416082282239.0)


if __name__ == '__main__':
  unittest.main()
