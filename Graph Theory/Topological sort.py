"""graph = {
    'A': ['D'],
    'B': ['D'],
    'C': ['A', 'B'],
    'D': ['G', 'H'],
    'E': ['A', 'D', 'F'],
    'F': ['J', 'K'],
    'G': ['I'],
    'H': ['I', 'J'],
    'I': ['L'],
    'J': ['L', 'M'],
    'K': ['J'],
    'L': [],
    'M': []
}"""

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['J'],
    'C' : ['F', 'I'],
    'D' : ['E', 'G'],
    'E' : ['K', 'H'],
    'F' : [],
    'G' : [],
    'H' : [],
    'I' : [],
    'J' : [],
    'K' : []
}

def dfs(at, visited, visitednodes, graph):
  visited[at] = True
  neighbours = graph[at]
  for i in neighbours:
    if not visited[i]:
      dfs(i, visited, visitednodes, graph)
  visitednodes.append(at)


def topsort(graph):
  n = len(graph)
  visited = {node: False for node in graph}
  result = []

  for at in graph:
    if visited[at] == False:
      visitednodes = []
      dfs(at, visited, visitednodes, graph)
      for nodeId in visitednodes:
        result.append(nodeId)
  return result

ordering = topsort(graph)
ordering.reverse()
print("Topological ordering: ", ordering)
