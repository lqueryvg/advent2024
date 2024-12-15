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
    p.grid = []
    p.moves = ''
    pass

  @patch('builtins.open')
  def test_tiny1(self, mock_open):
    mockOpen(mock_open, """
      #######
      #@..O..
      #......

      >
    """)
    self.assertEqual(p.main(), 104)

  @patch('builtins.open')
  def test_tiny2(self, mock_open):
    mockOpen(mock_open, """
      #######
      #@O....
      #......

      >>
    """)
    self.assertEqual(p.main(), 104)

  @patch('builtins.open')
  def test_example_small(self, mock_open):
    mockOpen(mock_open, """
      ########
      #..O.O.#
      ##@.O..#
      #...O..#
      #.#.O..#
      #...O..#
      #......#
      ########

      <^^>>>vv<v>>v<<
    """)
    self.assertEqual(p.main(), 2028)
    # self.assertEqual(p.someGlobal, ['1', '2024', '1', '9', '2021976', '0', '9'])

  @patch('builtins.open')
  def test_example_larger(self, mock_open):
    mockOpen(mock_open, """
      ##########
      #..O..O.O#
      #......O.#
      #.OO..O.O#
      #..O@..O.#
      #O#..O...#
      #O..O..O.#
      #.OO.O.OO#
      #....O...#
      ##########

      <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
      vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
      ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
      <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
      ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
      ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
      >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
      <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
      ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
      v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    """)
    self.assertEqual(p.main(), 10092)

class TestFindRobot(unittest.TestCase):
    def test_robot_found(self):
        p.height = 3
        p.width = 3
        p.grid = [['.', '.', '.'],
                ['.', '@', '.'],
                ['.', '.', '.']]
        self.assertEqual(p.findRobot(), (1, 1))

    def test_robot_not_found_empty_grid(self):
        p.height = 3
        p.width = 3
        p.grid = [['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.']]
        with self.assertRaises(Exception):
            p.findRobot()

    def test_robot_not_found(self):
        p.height = 3
        p.width = 3
        p.grid = [['.', '.', '.'],
                ['.', 'X', '.'],
                ['.', '.', '.']]
        with self.assertRaises(Exception):
            p.findRobot()

if __name__ == '__main__':
  unittest.main()
