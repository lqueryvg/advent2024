from typing import Any, Dict, Generator, List

f = 'input-example.txt'
f = 'input.txt'

type Graph = Dict[str, set[str]]

def addGraphEdge(graph: Graph, n1: str, n2: str) -> None:
  if n1 not in graph:
    graph[n1] = set()
  if n2 not in graph:
    graph[n2] = set()
  graph[n1].add(n2)
  graph[n2].add(n1)

def bron_kerbosch(graph: Graph) -> List[set[str]]:
  # Returns list of all maximal cliques, each is a set of nodes.
  def _bron_kerbosch(R: set[str], P: set[str], X: set[str]) -> Generator[set[str], Any, Any]:
    # R: the current clique being constructed
    # P: the set of candidate nodes to be added to the clique
    # X: the set of nodes already excluded from the clique
    if not P and not X:
      yield R
      return

    if not P: return

    # u: pivot node; the node with fewest neighbors; explore others first
    u = list(P)[0] 
    for v in P:
      if len(graph[v]) > len(graph[u]):
        u = v

    for v in list(P - graph[u]):
        new_R = R | {v} # add v
        new_P = P & graph[v] # P nodes which are neighbors of v
        new_X = X & graph[v] # X nodes which are neighbors of v
        yield from _bron_kerbosch(new_R, new_P, new_X)
        P.remove(v)
        X.add(v)
  
  return list(_bron_kerbosch(set(), set(graph.keys()), set()))

def go(lines):
  graph = {}
  for line in lines:
    (n1, n2) = line.split('-')
    addGraphEdge(graph, n1, n2)

  cliques = bron_kerbosch(graph)
  max_clique = {}
  for clique in cliques:
    if len(clique) > len(max_clique):
      max_clique = clique

  return ",".join(sorted(max_clique))

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    return go(lines)

if __name__ == '__main__':
  print(main())