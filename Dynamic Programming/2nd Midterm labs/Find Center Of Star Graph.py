def convert_to_matrix(edges, n):
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix

n = 6
edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
graph = convert_to_matrix(edges, n)

for row in graph:
  print(row)

def solution(graph):
  n = len(graph)
  star_center = []
  star_edges = []
  count = 0
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 1:
        count += 1
    if count == n-1:
      star_center.append(i)
    elif count == 1:
      star_edges.append(i)
    else:
      return "This graph isn't a star graph!"

    count = 0
  return "Center nodes:", star_center, "Edge nodes:", star_edges

solution(graph)