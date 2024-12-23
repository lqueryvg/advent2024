def bron_kerbosch(graph):
    """
    Finds all maximal cliques in a graph using the Bron-Kerbosch algorithm.

    Args:
        graph: A dictionary representing the graph where keys are vertices
               and values are sets of their neighbors.

    Returns:
        A list of sets, where each set represents a maximal clique.
    """

    def _bron_kerbosch(R, P, X):
        if not P and not X:
            yield R
            return

        # Pivoting (optional but improves performance significantly)
        if P:
          u = list(P)[0] # simple pivot selection, could be improved
          for v in list(P):
            if len(graph[v]) > len(graph[u]):
              u = v

          for v in list(P - graph[u]): # iterate over P \ N(u)
              new_R = R | {v}
              new_P = P & set(graph[v]) # Corrected line
              new_X = X & set(graph[v]) # Corrected line
              yield from _bron_kerbosch(new_R, new_P, new_X)
              P.remove(v)
              X.add(v)
        else:
          return # important for correctness when P is empty due to pivoting

    return list(_bron_kerbosch(set(), set(graph.keys()), set()))

# Example usage (same as before):
graph = {
    'A': {'B', 'C', 'D'},
    'B': {'A', 'C'},
    'C': {'A', 'B', 'D'},
    'D': {'A', 'C'},
    'E': {}
}

cliques = bron_kerbosch(graph)
print("Maximal Cliques:", cliques)

graph2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1, 3},
    3: {1, 2}
}

cliques2 = bron_kerbosch(graph2)
print("Maximal Cliques:", cliques2)

graph3 = {
    0: {1, 2, 3},
    1: {0, 2},
    2: {0, 1},
    3: {0}
}
cliques3 = bron_kerbosch(graph3)
print("Maximal Cliques:", cliques3)