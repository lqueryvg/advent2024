from typing import  TypeAlias, Literal
# f = 'input-tiny.txt'
# f = 'input-example.txt'
f = 'input.txt'

Point: TypeAlias = tuple[int, int]
Direction: TypeAlias = Literal["^", "v", "<", ">"]
offsets: dict[Direction, Point] = {
  "^": (0, -1),
  "v": (0, 1),
  "<": (-1, 0),
  ">": (1, 0)
}

def getGridValue(grid, p: Point) -> str:
  (x, y) = p
  return grid[y][x]

def offset(p: Point, direction: Direction) -> Point:
  (x, y) = p
  (dx, dy) = offsets[direction]
  return (x+dx, y+dy)

def findStartAndEnd(grid):
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      if getGridValue(grid, (x, y)) == 'S':
        start = (x, y)
      elif getGridValue(grid, (x, y)) == 'E':
        end = (x, y)
  return start, end

def notWall(grid, p: Point) -> bool:
  return getGridValue(grid, p) != '#'

def findCheats(grid):
  cheats: list[tuple[Point, Point]] = []
  # don't look at edges of grid
  for y in range(1, len(grid)-1):
    for x in range(1, len(grid[y])-1):
      if getGridValue(grid, (x, y)) == '#':
        p = (x, y)
        up, down = offset(p, "^"), offset(p, "v")
        if notWall(grid, up) and notWall(grid, down):
          cheats.append((up, down))
          continue # can't be both vertical and horizontal
        left, right = offset(p, "<"), offset(p, ">")
        if notWall(grid, left) and notWall(grid, right):
          cheats.append((left, right))
  return cheats


def printGrid(grid):
  print('--------------------------------')
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      print(getGridValue(grid, (x, y)), end='')
    print()
  print('--------------------------------')

def getStepData(grid, start, end):
  pointByStepnum: dict[int, Point] = {}
  stepnumByPoint: dict[Point, int] = {}
  visited: set[Point] = set()

  stepNum = 0
  currentPosition = start

  def add():
    nonlocal stepNum
    stepNum += 1
    pointByStepnum[stepNum] = currentPosition
    stepnumByPoint[currentPosition] = stepNum

  while currentPosition != end:
    add()
    visited.add(currentPosition)
    for direction in offsets:
      neighbor = offset(currentPosition, direction)
      if getGridValue(grid, neighbor) != '#':
        if neighbor not in visited:
          currentPosition = neighbor
          break

  add()

  return pointByStepnum, stepnumByPoint

def go(grid):

  start, end = findStartAndEnd(grid)
  pointByStepnum, stepnumByPoint = getStepData(grid, start, end)
  cheats = findCheats(grid)

  count = 0

  for cheat in cheats:
    l, r = cheat
    diff = abs(stepnumByPoint[r] - stepnumByPoint[l]) - 2
    if diff > 0:
      print(f"saves {diff}")

    if diff >= 100:
      count += 1
  return count

def main():
  global f
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    return go(grid)

if __name__ == '__main__':
  print(main())