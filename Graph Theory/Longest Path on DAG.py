g = {
    0: [(1, 3), (2, 6)],
    1: [(2, 4), (3, 4), (4, 11)],
    2: [(3, 8), (6, 11)],
    3: [(4, -4), (5, 5), (6, 2)],
    4: [(7, 9)],
    5: [(7, 1)],
    6: [(7, 2)],
    7: []
}


import heapq
from collections import deque

n = len(g)
s = 0

def topological_sort(g):
  in_degree = [0 for i in range(n)]
  for i in g:
    for v, w in g[i]:
      in_degree[v] += 1

  queue = deque()
  for i in range(n):
    if in_degree[i] == 0:
      queue.append(i)
  top_order = []

  while queue:
    at = queue.popleft()
    top_order.append(at)
    for v, w in g[at]:
      in_degree[v] -= 1
      if in_degree[v] == 0:
        queue.append(v)

  return top_order

def longest_path(g, n, s):
  top_order = topological_sort(g)
  dist = [float('-inf') for i in range(n)]
  dist[s] = 0

  for i in top_order:
    for v, w in g[i]:
      if dist[i] + w > dist[v]:
        dist[v] = dist[i] + w

  return dist

nodes = [i for i in g.keys()]

dist = longest_path(g, n, s)
for i in nodes:
  print("Longest path from", s, "->", i, "is", dist[i])