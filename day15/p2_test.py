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
    p.grid = []
    p.moves = ''
    pass

  @patch('builtins.open')
  def test_cost1(self, mock_open):
    mockOpen(mock_open, """
      ######
      #@.O..
      #.....

      >
    """)
    self.assertEqual(p.main(), 106)

  @patch('builtins.open')
  def test_cost2(self, mock_open):
    mockOpen(mock_open, """
      ######
      #@....
      #...O.

      >
    """)
    self.assertEqual(p.main(), 208)

  @patch('builtins.open')
  def test_cost3(self, mock_open):
    mockOpen(mock_open, """
      ######
      #@.O..
      #...O.

      >
    """)
    self.assertEqual(p.main(), 314)

  @patch('builtins.open')
  def test_horizontal_move1(self, mock_open):
    mockOpen(mock_open, """
      #####
      #@OO.

      >>
    """)
    self.assertEqual(p.main(), 212)

  @patch('builtins.open')
  def test_horizontal_move2(self, mock_open):
    mockOpen(mock_open, """
      ########
      #@OO.O.#

      >>>>>>>
    """)
    self.assertEqual(p.main(), 330)

  @patch('builtins.open')
  def test_vertical_move1(self, mock_open):
    mockOpen(mock_open, """
      ####
      #...
      #OOO
      #.@.

      ^
    """)
    self.assertEqual(p.main(), 512)

  @patch('builtins.open')
  def test_move1(self, mock_open):
    mockOpen(mock_open, """
      #######
      #.....#
      #..O..#
      #..O..#
      #..@..#
      #######

      ^
    """)
    self.assertEqual(p.main(), 312)
    
  @patch('builtins.open')
  def test_move2(self, mock_open):
    mockOpen(mock_open, """
      #######
      #.....#
      #..O..#
      #.....#
      #..O..#
      #..@..#
      #######

      ^^
    """)
    self.assertEqual(p.main(), 312)

  @patch('builtins.open')
  def test_move3(self, mock_open):
    mockOpen(mock_open, """
      #####
      #...#
      #.O@#
      #O..#
      #...#
      #####

      <vv<<^
    """)
    self.assertEqual(p.main(), 305)

  @patch('builtins.open')
  def test_move4(self, mock_open):
    mockOpen(mock_open, """
      #######
      #...#.#
      #.....#
      #..OO@#
      #..O..#
      #.....#
      #######

      <vv<<^^<<^^
    """)
    self.assertEqual(p.main(), 618)

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
    self.assertEqual(p.main(), 1751)
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
    self.assertEqual(p.main(), 9021)

if __name__ == '__main__':
  unittest.main()
