adj_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]



def BFS(adj_matrix, start):
  n = len(adj_matrix)
  visited = set()
  queue = [start]
  visited.add(start)


  while queue:
    node = queue.pop(0)
    print(node, end="-->")

    for i in range(n):
      if adj_matrix[node][i] == 1 and i not in visited:
        visited.add(i)
        queue.append(i)


BFS(adj_matrix, 0)
