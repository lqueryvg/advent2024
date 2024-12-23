f = 'input-example.txt'
f = 'input.txt'

from typing import Dict, List
type Graph = Dict[str, List[str]]

def addEdge(graph: Graph, n1: str, n2: str) -> None:
  if n1 not in graph:
    graph[n1] = []
  if n2 not in graph:
    graph[n2] = []
  graph[n1].append(n2)
  graph[n2].append(n1)

def go(lines):
  graph: Graph = {}
  for line in lines:
    (n1, n2) = line.split('-')
    addEdge(graph, n1, n2)

  s = set()
  for n1 in graph:
    if not n1.startswith("t"): continue
    for l in range(0, len(graph[n1])):
      n2 = graph[n1][l]
      for r in range(l + 1, len(graph[n1])):
        n3 = graph[n1][r]
        if n3 in graph[n2]:
          s.add(",".join(sorted([n1, n2, n3])))

  return len(s)

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    return go(lines)

if __name__ == '__main__':
  print(main())