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


def isBlocked(robot, direction) -> bool:
  r = robot
  while True:
    r = offset(r, direction)
    v = getGridValue(r)
    if v == '.':
      return False
    if v == '#':
      return True

def moveRobot(robot: Point, direction: Direction) -> Point:
  # look ahead to see if there is an empty space before finding a wall

  if isBlocked(robot, direction):
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


def cost() -> int:
  total = 0
  for y in range(0, height):
    for x in range(0, width):
      p = (x, y)
      if getGridValue(p) == 'O':

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
        grid.append(line)
        continue
      moves += line

    width = len(grid[0])
    height = len(grid)

    return go()

if __name__ == '__main__':
  print(main())