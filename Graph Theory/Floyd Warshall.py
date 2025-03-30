m = [
    [0,   5,   0,   0,   0,   0,   0,   0,   0,   0],
    [0,   0,  20,   0,   0,  30,  60,   0,   0,   0],
    [0,   0,   0,  10,  75,   0,   0,   0,   0,   0],
    [0,   0, -15,   0,   0,   0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0,   0,   0,   0,   0, 100],
    [0,   0,   0,   0,  25,   0,   5,   0,  50,   0],
    [0,   0,   0,   0,   0,   0,   0, -50,   0,   0],
    [0,   0,   0,   0,   0,   0,   0,   0, -10,   0],
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
]

n = len(m)
dp = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
  for j in range(n):
    if m[i][j] == 0 and i != j:
      dp[i][j] = float('inf')
    else:
      dp[i][j] = m[i][j]

next = [[-1 for i in range(n)] for j in range(n)]
for i in range(n):
  for j in range(n):
    if m[i][j] != 0:
      next[i][j] = j

def floyd_warshall(m, n):
  setup(m)

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dp[i][k] + dp[k][j] < dp[i][j]:
          dp[i][j] = dp[i][k] + dp[k][j]
          next[i][j] = next[i][k]

  propagateNegativeCycle(dp, n)

  return dp

def setup(m):
  dp = [[0 for i in range(n)] for j in range(n)]
  next = [[0 for i in range(n)] for j in range(n)]

  for i in range(n):
    for j in range(n):
      dp[i][j] = m[i][j]
      if m[i][j] != 0:
        next[i][j] = j

def propagateNegativeCycle(dp, n):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dp[i][k] + dp[k][j] < dp[i][j]:
          dp[i][j] = -float('inf')
          next[i][j] = -1

dp = floyd_warshall(m, n)
for row in dp:
  for element in row:
    if element == float('inf'):
      print(" ∞ ", end=" ")
    elif element == -float('inf'):
      print("-∞ ", end=" ")
    else:
      print(element, end="  ")
  print()

negative_cycle = False
for i in range(n):
  if dp[i][i] != 0:
    negative_cycle = True
    break

if negative_cycle:
  print("Negative cycle found!")
else:
  print("No negative cycle found!")
