from __future__ import annotations
from typing import  TypeAlias, Literal
from typing import cast
import math
import heapq

f = 'input.txt'

grid = []
width = 0
height = 0
start = (0,0)
end = (0,0)
depth = 0
minCost = math.inf
# cache: dict[Deer, float] = {}
fictiousEndNode = ((1000,1000), '^')


Point: TypeAlias = tuple[int, int]
Direction: TypeAlias = Literal["^", "v", "<", ">"]
Deer: TypeAlias = tuple[Point, Direction]
offsets = {
  "^": (0, -1),
  "v": (0, 1),
  "<": (-1, 0),
  ">": (1, 0)
}

clockwise: dict[Direction, Direction] = {
  "^": ">",
  ">": "v",
  "v": "<",
  "<": "^"
}

counterclockwise: dict[Direction, Direction] = {
  "^": "<",
  "<": "v",
  "v": ">",
  ">": "^"
}

opposites: dict[Direction, Direction] = {
  "^": "v",
  "<": ">",
  "v": "^",
  ">": "<"
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


def printGrid():
  print('--------------------------------')
  for y in range(0, height):
    for x in range(0, width):
      print(getGridValue((x, y)), end='')
    print()
  print('--------------------------------')

def buildGraph():
  graph: dict[Deer, list[tuple[Deer, float]]] = {}
  for y in range(0, height):
    for x in range(0, width):
      p = (x,y)
      v = getGridValue(p)
      if v == '#': continue

      for d in offsets:
        direction = cast(Direction, d)

        graph[(p, direction)] = []
        n = offset(p, direction)
        if getGridValue(n) != '#':
          graph[(p, direction)].append(((n, direction), 1))
        graph[(p, direction)].append(((p, clockwise[direction]), 1000))
        graph[(p, direction)].append(((p, counterclockwise[direction]), 1000))
  
  # add ficticious end node
  graph[fictiousEndNode] = []
  for d in offsets:
    direction = cast(Direction, d)
    graph[(end, direction)] = [(fictiousEndNode, 0)]
  

  return graph

def all_shortest_paths_weighted(graph, start, end):
  distances = {node: float('inf') for node in graph}
  predecessors = {node: [] for node in graph}
  distances[start] = 0
  pq = [(0, start)]  # (distance, node)

  while pq:
    dist, u = heapq.heappop(pq)

    if dist > distances[u]:
      continue

    for v, weight in graph[u]:
      new_dist = distances[u] + weight
      if new_dist < distances[v]:
        distances[v] = new_dist
        predecessors[v] = [u]
        heapq.heappush(pq, (new_dist, v))
      elif new_dist == distances[v]:
        predecessors[v].append(u)

  def reconstruct_paths(current, path):
    if current == start:
      all_paths.append(path)
      return

    for prev in predecessors.get(current, []):
      reconstruct_paths(prev, [prev] + path)

  all_paths = []
  reconstruct_paths(end, [end])
  return all_paths

def go(graph):
  paths = all_shortest_paths_weighted(graph, (start, '<'), fictiousEndNode)
  nodes = set()
  for path in paths:
    for node in path:
      p, _d = node
      nodes.add(p)

  nodes.add(start)
  nodes.add(end)
  nodes.remove((1000,1000))
  return len(nodes)


def main():
  global f, grid, width, height, start, end
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]

    width = len(grid[0])
    height = len(grid)
    start = (1, height - 2)
    end = (width - 2, 1)
    graph = buildGraph()

    return go(graph)

if __name__ == '__main__':
  print(main())