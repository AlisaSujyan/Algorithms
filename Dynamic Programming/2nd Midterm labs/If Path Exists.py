def Path_exisits(n, edges, start, destination):
  graph = {i: [] for i in range(n)}

  for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

  print(graph)

  queue = [start]
  visited = set()

  while queue:
    node = queue.pop(0)
    if node == destination:
      return True

    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        queue.append(neighbor)

  return False

n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]

destination = 5

start = 0

path = Path_exisits(n, edges, start, destination)
if path:
  print("There is a path from", start, "to", destination)
else:
  print("There is no path from", start, "to", destination)


start = 3

path = Path_exisits(n, edges, start, destination)
if path:
  print("There is a path from", start, "to", destination)
else:
  print("There is no path from", start, "to", destination)