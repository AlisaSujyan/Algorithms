def RedundantConnection(edges):

  def cycle(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        if cycle(graph, neighbor, visited, node):
          return True
      elif neighbor != parent:
        return True
    return False

  graph = {}

  for u, v in edges:

    if u not in graph:
      graph[u] = []
    if v not in graph:
      graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

    visited = set()
    if cycle(graph, u, visited, -1):
      print(graph)
      return [u, v]

  return []

edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
          [2, 6], [3, 7], [3, 8], [4, 9], [4, 10],
          [5, 11], [5, 12], [6, 12]]

print("The Redundant Connection is: ", RedundantConnection(edges))