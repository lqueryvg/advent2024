from typing import Set
from typing import TypeAlias

f = 'input.txt'

grid = []

Coord: TypeAlias = tuple[int, int]
Path: TypeAlias = tuple[Coord, Coord]

visited: Set[Coord] = set()
pathsSeen: Set[Path] = set()

def isOutOfBounds(x: int, y: int) -> bool:
  return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def hasBorder(p1: Coord, p2: Coord) -> bool:
  (x1, y1) = p1
  (x2, y2) = p2
  if isOutOfBounds(x2, y2):
    return True
  return grid[y1][x1] != grid[y2][x2] 

def getBorders(x: int, y: int) -> set:  # returns set of borders e.g. {"T","B","L","R"}
  if isOutOfBounds(x, y):
    return set()
  
  s = set()
  v = grid[y][x]
  if hasBorder((x, y), (x+1, y)):
    s.add("R")
  if hasBorder((x, y), (x-1, y)):
    s.add("L")
  if hasBorder((x, y), (x, y+1)):
    s.add("B")
  if hasBorder((x, y), (x, y-1)):
    s.add("T")
  return s
  
def getCommonBorders(s1: set, s2: set) -> set:
  return s1.intersection(s2)

def addPath(p1: tuple[int, int], p2: tuple[int, int]):
  pathsSeen.add((p1, p2))
  pathsSeen.add((p2, p1))

def go(
  x: int, 
  y: int, 
  plant: str, 
  prevBorders: set, 
  fromCoord: tuple[int, int]
) -> tuple[int, int]: 
  # returns (area, fences)

  # check end conditions

  if isOutOfBounds(x, y):
    return (0, 0)
  
  # different plant
  if grid[y][x] != plant:
    return (0, 0)

  thisBorders = getBorders(x, y)

  if (x, y) in visited:
    # same plant, already visited
    if (fromCoord, (x, y)) in pathsSeen:
      return (0, 0) # add nothing
    else:
      minus = len(getCommonBorders(thisBorders, prevBorders))
      addPath(fromCoord, (x, y))
      return (0, -minus)
  
  # same plant, not visited yet

  addPath(fromCoord, (x, y))
  visited.add((x, y))
  area = 1
  fences = len(thisBorders) - len(getCommonBorders(thisBorders, prevBorders))

  for direction in [ [1,0], [0,1], [0,-1], [-1,0] ]:
    dx, dy = direction
    x1 = x + dx
    y1 = y + dy

    (a, f) = go(x1, y1, plant, thisBorders, (x, y))
    area += a
    fences += f
  
  return (area, fences)


def main():
  global f, grid
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    
    cost = 0
    for y in range(0, len(grid)):
      for x in range(0, len(grid[y])):
        (area, fences) = go(x, y, grid[y][x], set(), (-1,-1))
        cost += area * fences

    return cost

if __name__ == '__main__':
  print(main())