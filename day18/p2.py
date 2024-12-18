from __future__ import annotations
from typing import  TypeAlias, Literal
from typing import cast
import math
from collections import deque

f = 'input.txt'
width = 71
height = 71

# f = 'input-example.txt'
# width = 7
# height = 7

start = (0,0)
rockNumbers: dict[Point, int] = {}
allRocks: list[Point] = []
minCost = math.inf

Point: TypeAlias = tuple[int, int]
Direction: TypeAlias = Literal["^", "v", "<", ">"]
offsets = {
  "^": (0, -1),
  "v": (0, 1),
  "<": (-1, 0),
  ">": (1, 0)
}

def isOutOfBounds(p: Point) -> bool:
  (x, y) = p
  return x < 0 or x >= width or y < 0 or y >= height

def offset(p: Point, direction: Direction) -> Point:
  (x, y) = p
  (dx, dy) = offsets[direction]
  return (x+dx, y+dy)

def isRock(p: Point, numRocks) -> bool:
  return p in rockNumbers and rockNumbers[p] <= numRocks

def buildGraph(numRocks):
  graph: dict[Point, list[Point]] = {}
  for y in range(0, height):
    for x in range(0, width):
      p = (x,y)

      if isRock(p, numRocks): continue

      graph[p] = []
      for d in offsets:
        direction = cast(Direction, d)
        n = offset(p, direction) # neighbor
        if isOutOfBounds(n) or isRock(n, numRocks): continue
        graph[p].append(n)
  
  return graph


def blocked(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return False

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return True

def go():

  low = 0
  high = len(rockNumbers) - 1
  goal = (width-1, height-1)
  mid = (low + high) // 2

  while low <= high:
    mid = (low + high) // 2
    graph = buildGraph(mid)
    if blocked(graph, start, goal):
      high = mid - 1
    else:
      low = mid + 1
  
  return mid + 1

def main():
  global f
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    rockNum = 0
    for line in lines:
       (x, y) = line.split(',')
       rockNumbers[(int(x), int(y))] = rockNum
       allRocks.append((int(x), int(y)))
       rockNum += 1

    return allRocks[go()]

if __name__ == '__main__':
  print(main())