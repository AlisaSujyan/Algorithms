g = {
    0: [(1, 4), (2, 1)],
    1: [(1, 1)],
    2: [(2, 1), (3, 5)],
    3: [(4, 3)],
    4: []
}


import heapq

n = len(g)
s = 0

def dijkstra(g, n, s):
  visited = [False for i in range(n)]
  prev = [-1 for i in range(n)]
  dist = [float('inf') for i in range(n)]
  dist[s] = 0
  pq = []
  heapq.heappush(pq, (0, s))

  while pq:
    minValue, index = heapq.heappop(pq)

    if visited[index]:
      continue
    visited[index] = True

    if dist[index] < minValue:
      continue

    for neighbor, weight in g[index]:
      if visited[neighbor]:
        continue
      newDist = dist[index] + weight
      if newDist < dist[neighbor]:
        dist[neighbor] = newDist
        prev[neighbor] = index
        heapq.heappush(pq, (newDist, neighbor))


  return prev, dist

prev, dist = dijkstra(g, n, s)
nodes = [i for i in g.keys()]

for i in nodes:
  print("Longest path from", s, "->", i, "is", dist[i])