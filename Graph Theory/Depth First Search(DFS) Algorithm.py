graph = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n = len(graph)
visited = [False for i in range(n)]
result = []


def dfs(at):
  if visited[at]:
    return
  visited[at] = True
  neighbours = graph[at]
  for i in range(n):
    if neighbours[i] == 1:
      dfs(i)
  result.append(at)
  visited[at] = True
  return result

result = dfs(0)
result.reverse()

for i in range(len(result)):
  if i != len(result) - 1:
    print(result[i], end="-->")
  elif i == len(result) - 1:
    print(result[i])