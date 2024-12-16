from __future__ import annotations
from typing import  TypeAlias, Literal
from typing import cast

f = 'input.txt'

grid = []
moves: str = ''
width = 0
height = 0

Point: TypeAlias = tuple[int, int]
Direction: TypeAlias = Literal["^", "V", "<", ">"]
offsets = {
  "^": (0, -1),
  "v": (0, 1),
  "<": (-1, 0),
  ">": (1, 0)
}

def getGridValue(p: Point) -> str:
  (x, y) = p
  return grid[y][x]

def setGridValue(p: Point, value: str):
  (x, y) = p
  grid[y] = grid[y][:x] + value + grid[y][x+1:]


def offset(p: Point, direction: Direction) -> Point:
  (x, y) = p
  (dx, dy) = offsets[direction]
  return (x+dx, y+dy)

def findRobot() -> Point:
  for y in range(0, height):
    for x in range(0, width):
      p = (x, y)
      if getGridValue(p) == '@':
        return p

  raise Exception(f"Unable to find robot")

  

def isBox(c) -> bool:
  return c == '[' or c == ']'

def boxCanMoveVertically(p: Point, direction: Direction) -> bool:
  v = getGridValue(p)
  # adjust p to point at left edge of box
  if v == ']':
    p = offset(p, '<')
    v = '['

  p1 = p
  p2 = offset(p1, '>')

  # the 2 points above or below box
  d1 = offset(p1, direction)
  d2 = offset(p2, direction)

  v1 = getGridValue(d1)
  v2 = getGridValue(d2)


  # end cases
  if v1 == '#' or v2 == '#': return False
  if v1 == '.' and v2 == '.':
    return True

  # recursive cases
  if v1 == '[':
    return boxCanMoveVertically(d1, direction)

  if v1 == ']' and v2 == '.':
    return boxCanMoveVertically(d1, direction)

  if v1 == '.' and v2 == '[':
    return boxCanMoveVertically(d2, direction)

  if v1 == ']' and v2 == '[':
    return boxCanMoveVertically(d1, direction) and boxCanMoveVertically(d2, direction)

  raise Exception(f"Unknown case {v1=}, {v2=}")

def moveBoxVertically(p: Point, direction: Direction):
  v = getGridValue(p)
  # adjust p to point at left edge of box
  if v == '.':
    return
  if v == ']':
    p = offset(p, '<')
    v = '['

  p1 = p
  p2 = offset(p1, '>')

  # the 2 points above or below box
  d1 = offset(p1, direction)
  d2 = offset(p2, direction)

  v1 = getGridValue(d1)
  v2 = getGridValue(d2)


  def moveBox():
    setGridValue(d1, '[')
    setGridValue(d2, ']')
    setGridValue(p1, '.')
    setGridValue(p2, '.')

  # end cases
  if v1 == '.' and v2 == '.':
    moveBox()

  # recursive cases
  if v1 == '[':
    if moveBoxVertically(d1, direction):
      moveBox()

  if v1 == ']':
    moveBoxVertically(d1, direction)

  if v2 == '[':
    moveBoxVertically(d2, direction)

  moveBox()

def moveRobotVertically(robot: Point, direction: Direction) -> Point:
  p1 = offset(robot, direction)
  v = getGridValue(p1)
  if v == '#':
    return robot
  
  if isBox(v):
    if boxCanMoveVertically(p1, direction):
      moveBoxVertically(p1, direction)
    else:
      return robot

  setGridValue(robot, '.')
  setGridValue(p1, '@')
  return p1

  
def isHorizontallyBlocked(robot, direction) -> bool:
  r = robot
  while True:
    r = offset(r, direction)
    v = getGridValue(r)
    if v == '.':
      return False
    if v == '#':
      return True

def moveRobotHorizontal(robot: Point, direction: Direction) -> Point:

  if isHorizontallyBlocked(robot, direction):
    return robot

  v = '.'
  l = robot
  def swap(l, v):
    temp = getGridValue(l)
    setGridValue(l, v)
    return temp

  while True:
    v = swap(l, v)
    l = offset(l, direction)
    if v == '.':
      break

  return offset(robot, direction)

def moveRobot(robot: Point, direction: Direction) -> Point:
  if direction == '^' or direction == 'v':
    return moveRobotVertically(robot, direction)
  
  return moveRobotHorizontal(robot, direction)

def cost() -> int:
  total = 0
  for y in range(0, height):
    for x in range(0, width):
      p = (x, y)
      if getGridValue(p) == '[':

        total += (100 * y) + x
  return total

def printGrid():
  print('--------------------------------')
  for y in range(0, height):
    for x in range(0, width):
      print(getGridValue((x, y)), end='')
    print()
  print('--------------------------------')

def go():
  robot = findRobot()
  for move in moves:
    robot = moveRobot(robot, cast(Direction, move))
  return cost()

def widenLine(line: str) -> str:
  newLine = ''
  for c in line:
    if c == '@':
      newLine += '@.'
    elif c == '.':
      newLine += '..'
    elif c == '#':
      newLine += '##'
    elif c == 'O':
      newLine += '[]'
  return newLine

def main():
  global f, grid, moves, width, height
  with open(f) as f:
    lines = f.readlines()
    isGrid = True
    for line in lines:
      line = line.strip()
      if line == '':
        isGrid = False
        continue
      if isGrid:
        grid.append(widenLine(line))
        continue
      moves += line

    width = len(grid[0])
    height = len(grid)

    return go()

if __name__ == '__main__':
  print(main())