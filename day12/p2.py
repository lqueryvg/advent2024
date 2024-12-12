from typing import Set, TypeAlias, Literal

f = 'input.txt'

grid = []

Coord: TypeAlias = tuple[int, int]
Path: TypeAlias = tuple[Coord, Coord]
Fence: TypeAlias = Literal["T", "B", "L", "R"]
Fences: TypeAlias = set[Fence]

visited: Set[Coord] = set()
pathsSeen: Set[Path] = set()

def getGridValue(p: Coord) -> str:
  (x, y) = p
  return grid[y][x]

def isOutOfBounds(p: Coord) -> bool:
  (x, y) = p
  return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def hasFenceBetween(p1: Coord, p2: Coord) -> bool:
  if isOutOfBounds(p2):
    return True
  return getGridValue(p1) != getGridValue(p2)

def getFences(p: Coord) -> Fences:  # returns set of fences e.g. {"T","B","L","R"}
  if isOutOfBounds(p):
    return set()
  
  (x, y) = p
  s: Fences = set()
  if hasFenceBetween(p, (x+1, y)):
    s.add("R")
  if hasFenceBetween(p, (x-1, y)):
    s.add("L")
  if hasFenceBetween(p, (x, y+1)):
    s.add("B")
  if hasFenceBetween(p, (x, y-1)):
    s.add("T")
  return s
  
def getCommonFences(s1: Fences, s2: Fences) -> Fences:
  return s1.intersection(s2)


def addPath(p1: Coord, p2: Coord):
  pathsSeen.add((p1, p2))
  pathsSeen.add((p2, p1))

def go(
  currentCoord: Coord,
  plantType: str, 
  prevFences: Fences, 
  prevCoord: Coord
) -> Coord: 
  # returns (area, fences)

  # check end conditions

  if isOutOfBounds(currentCoord):
    return (0, 0)
  
  (x, y) = currentCoord
  
  # different plant
  if getGridValue(currentCoord) != plantType:
    return (0, 0)

  currentFences = getFences(currentCoord)

  if currentCoord in visited:
    # same plant, already visited
    if (prevCoord, currentCoord) in pathsSeen:
      return (0, 0) # add nothing
    else:
      minus = len(getCommonFences(currentFences, prevFences))
      addPath(prevCoord, currentCoord)
      return (0, -minus)
  
  # same plant, not visited yet

  addPath(prevCoord, currentCoord)

  visited.add(currentCoord)
  area = 1
  numFences = len(currentFences) - len(getCommonFences(currentFences, prevFences))

  for direction in [ [1,0], [0,1], [0,-1], [-1,0] ]:
    dx, dy = direction
    x1 = x + dx
    y1 = y + dy

    (a, f) = go((x1, y1), plantType, currentFences, currentCoord)
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
        p: Coord = (x, y)
        (area, fences) = go(p, getGridValue(p), set(), (-1,-1))
        cost += area * fences

    return cost

if __name__ == '__main__':
  print(main())