from typing import  TypeAlias, Literal
from collections import Counter
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

def manhattan(p1: Point, p2: Point) -> int:
  (x1, y1) = p1
  (x2, y2) = p2
  return abs(x1 - x2) + abs(y1 - y2)

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
    pointByStepnum[stepNum] = currentPosition
    stepnumByPoint[currentPosition] = stepNum
    stepNum += 1

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

def countCheats(pointByStepnum):
  countsBySaving = Counter()
  count = 0
  cheatsSeen = set()
  minDiffWanted = 100
  # minDiffWanted = 0
  # minDiffWanted = 50

  numSteps = len(pointByStepnum)
  print(f"{numSteps=}")
  for l in range(0, numSteps):
    for r in range(l + 4, numSteps):
      trackSteps = abs(r - l)
      lp = pointByStepnum[l]
      rp = pointByStepnum[r]
      m = manhattan(lp, rp)
      if m > 20:
        continue

      saving = trackSteps - m
      if saving < minDiffWanted or saving <= 0:
        continue
      
      t = (min(lp, rp), max(lp, rp))
      if not t in cheatsSeen:
        cheatsSeen.add(t)
        countsBySaving.update({saving: 1})
        count += 1

  return count

def go(grid):
  start, end = findStartAndEnd(grid)
  pointByStepnum, stepnumByPoint = getStepData(grid, start, end)
  return countCheats(pointByStepnum)

def main():
  global f
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    return go(grid)

if __name__ == '__main__':
  print(main())