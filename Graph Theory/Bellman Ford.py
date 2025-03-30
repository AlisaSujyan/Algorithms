g = {
    0: [(1, 5)],
    1: [(2, 20), (5, 30), (6, 60)],
    2: [(3, 10), (4, 75)],
    3: [(2, -15)],
    4: [(9, 100)],
    5: [(4, 25), (6, 5), (8, 50)],
    6: [(7, -50)],
    7: [(8, -10)],
    8: [],
    9: []
}

def BellmanFord(g, s):
  n = len(g)
  dist = [float('inf') for i in range(n)]
  dist[s] = 0
  affected_nodes = []

  for i in range(n-1):
    for u in g:
      for v, w in g[u]:
        if dist[v] > dist[u] + w:
          dist[v] = dist[u] + w
  dist_1 = dist.copy()

  for u in g:
    for v, w in g[u]:
      if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        affected_nodes.append(v)
  nodes = [i for i in g.keys()]

  for i in nodes:
    print("Shortest path from", s, "->", i, "is", dist[i])
  print("Affected nodes:", affected_nodes)

BellmanFord(g, 0)