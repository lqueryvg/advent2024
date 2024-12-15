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

# def isOutOfBounds(p: Point) -> bool:
#   (x, y) = p
#   return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)


def offset(p: Point, direction: Direction) -> Point:
  (x, y) = p
  (dx, dy) = offsets[direction]
  return (x+dx, y+dy)

def findRobot() -> Point:
  # print("hello")
  for y in range(0, height):
    for x in range(0, width):
      p = (x, y)
      # print(f"{p=}, {getGridValue(p)}")
      if getGridValue(p) == '@':
        return p

  raise Exception(f"Unable to find robot")

def moveRobot(robot: Point, direction: Direction) -> Point:
  # look ahead to see if there is an empty space before finding a wall
  r = robot
  while True:
    r = offset(r, direction)
    v = getGridValue(r)
    if v == '.':
      break
    if v == '#':
      return robot
    
  # now we know that we can move and / or push
  # replace the robot with an empty space
  # set all subsequent cells to 'O' up to and including the first empty space
  # finally set and return the new robot position

  setGridValue(robot, '.')
  # robot = offset(robot, direction)
  l = robot
  while True:
    l = offset(l, direction)
    v = getGridValue(l)
    setGridValue(l, 'O')
    if v == '.':
      break
  robot = offset(robot, direction)
  setGridValue(robot, '@')
  return robot

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
  # print(f"{width=}, {height=}, {moves=}, {grid=}")
  robot = findRobot()
  # printGrid()
  for move in moves:
    robot = moveRobot(robot, cast(Direction, move))
    print(f"{move=}, {robot=}")
    # printGrid()
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