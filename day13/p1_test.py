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

  def test_calculate_machine1(self):
    self.assertEqual(p.calculate(8400,	5400,	94,	34,	22,	67), 280)

  def test_calculate_machine2(self):
    self.assertEqual(p.calculate(12748, 12176, 26, 66, 67, 21), 0)

  def test_calculate_machine3(self):
    self.assertAlmostEqual(p.calculate(7870, 6450, 17, 86,84, 37), 200)

  def test_calculate_machine4(self):
    self.assertEqual(p.calculate(18641, 10279, 69, 23, 27, 71), 0)

  @patch('builtins.open')
  def test_machines(self, mock_open):
    mockOpen(mock_open, """
      Button A: X+94, Y+34
      Button B: X+22, Y+67
      Prize: X=8400, Y=5400

      Button A: X+26, Y+66
      Button B: X+67, Y+21
      Prize: X=12748, Y=12176

      Button A: X+17, Y+86
      Button B: X+84, Y+37
      Prize: X=7870, Y=6450

      Button A: X+69, Y+23
      Button B: X+27, Y+71
      Prize: X=18641, Y=10279
    """)
    self.assertEqual(p.main(), 480)

if __name__ == '__main__':
  unittest.main()
