from __future__ import annotations
from typing import Set, TypeAlias, Literal

f = 'input.txt'

grid = []

Point: TypeAlias = tuple[int, int]
Path: TypeAlias = tuple[Point, Point]
Direction: TypeAlias = Literal["U", "D", "L", "R"]
Fences: TypeAlias = set[Direction]
allDirections: list[Direction] = ["U", "D", "L", "R"]
offsets = {
  "U": (0, -1),
  "D": (0, 1),
  "L": (-1, 0),
  "R": (1, 0)
}

visited: Set[Point] = set()
pathsSeen: Set[Path] = set()

def getGridValue(p: Point) -> str:
  (x, y) = p
  return grid[y][x]

def isOutOfBounds(p: Point) -> bool:
  (x, y) = p
  return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)


def offset(p: Point, direction: Direction) -> Point:
  (x, y) = p
  (dx, dy) = offsets[direction]
  return (x+dx, y+dy)


def hasFenceBetween(p1: Point, p2: Point) -> bool:
  if isOutOfBounds(p2):
    return True
  return getGridValue(p1) != getGridValue(p2)

def getFences(p: Point) -> Fences:  # returns set of fences e.g. {"U","D","L","R"}
  if isOutOfBounds(p):
    return set()
  
  s: Fences = set()
  for direction in allDirections:
    if hasFenceBetween(p, offset(p, direction)):
      s.add(direction)
  return s
  
def getCommonFences(s1: Fences, s2: Fences) -> Fences:
  return s1.intersection(s2)

def recordReturnPath(p1: Point, p2: Point):
  pathsSeen.add((p2, p1))

def pathAlreadySeen(p1: Point, p2: Point) -> bool:
    return (p2, p1) in pathsSeen

def go(
  currentPoint: Point,
  plantType: str, 
  prevFences: Fences, 
  prevPoint: Point
) -> tuple[int, int]: 
  # returns (area, fences)

  # check end conditions

  if isOutOfBounds(currentPoint):
    return (0, 0)
  
  # different plant
  if getGridValue(currentPoint) != plantType:
    return (0, 0)

  currentFences = getFences(currentPoint)

  if currentPoint in visited:
    # same plant, already visited
    if pathAlreadySeen(currentPoint, prevPoint):
      return (0, 0) # add nothing
    else:
      # we've approached this point from a new direction
      # (made a loop) so we need to make an adjustment to the number of fences
      # to cater for common fences which have already been counted
      adjustment = - len(getCommonFences(currentFences, prevFences))
      recordReturnPath(prevPoint, currentPoint)
      return (0, adjustment)
  
  # same plant, not visited yet

  recordReturnPath(prevPoint, currentPoint)

  visited.add(currentPoint)
  area = 1
  numFences = len(currentFences) - len(getCommonFences(currentFences, prevFences))

  for direction in allDirections:
    p1 = offset(currentPoint, direction)
    (a, f) = go(p1, plantType, currentFences, currentPoint)
    area += a
    numFences += f
  
  return (area, numFences)


def main():
  global f, grid
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    
    cost = 0
    for y in range(0, len(grid)):
      for x in range(0, len(grid[y])):
        p: Point = (x, y)
        (area, fences) = go(p, getGridValue(p), set(), (-1,-1))
        cost += area * fences

    return cost

if __name__ == '__main__':
  print(main())