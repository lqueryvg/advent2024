from __future__ import annotations
import sys
from typing import  TypeAlias, Literal
from typing import cast
import math
from collections import deque

f = 'input.txt'
# f = 'input-example.txt'

maxRocks = 1024
grid = []

width = 71
height = 71
start = (0,0)
end = (70,70)
minCost = math.inf

rocks = set()

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

def isRock(p: Point) -> bool:
   return p in rocks

def getGridValue(p: Point) -> str:
  return '#' if isRock(p) else '.'

def printGrid():
  print('--------------------------------')
  for y in range(0, height):
    for x in range(0, width):
      print(getGridValue((x, y)), end='')
    print()
  print('--------------------------------')

def buildGraph():
  graph: dict[Point, list[Point]] = {}
  for y in range(0, height):
    for x in range(0, width):
      p = (x,y)

      if isRock(p): continue

      graph[p] = []
      for d in offsets:
        direction = cast(Direction, d)
        n = offset(p, direction) # neighbor
        if isOutOfBounds(n) or isRock(n): continue
        graph[p].append(n)
  
  return graph


def bfs_shortest_path(graph, start, goal):
  queue = deque([(start, [start])])
  visited = set([start])

  while queue:
    node, path = queue.popleft()
    if node == goal:
      return path
    for neighbor in graph.get(node, []):
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, path + [neighbor]))

  raise ValueError(f"Could not find a path from {start} to {goal}.")

def go(graph):
  path = bfs_shortest_path(graph, start, (width-1, height-1))
  return len(path) - 1

def main():
  global f
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    count = 0
    for line in lines:
       count += 1
       if count > maxRocks: break
       (x, y) = line.split(',')
       rocks.add((int(x), int(y)))

    graph = buildGraph()

    return go(graph)

if __name__ == '__main__':
  print(main())