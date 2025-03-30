# "S" is the starting point
# "E" is the end
# "." is an empty cell
# "#" is a cell full of rock

from queue import Queue
import numpy as np

m = [["S", ".", ".", "#", ".", ".", "."],
     [".", "#", ".", ".", ".", "#", "."],
     [".", "#", ".", ".", ".", ".", "."],
     [".", ".", "#", "#", ".", ".", "."],
     ["#", ".", "#", "E", ".", "#", "."]]

R = len(m)
C = len(m[0])

for i, row in enumerate (m):
  for j, val in enumerate(row):
    if val == "S":
      sr, sc = i, j
    elif val == "E":
      er, ec = i, j

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def explore_neighbours(r, c):
  neighbours = []
  for i in range(4):
    rr, cc = r + dr[i], c + dc[i]
    if rr < 0 or rr >= R or cc < 0 or cc >= C:
      continue
    if m[rr][cc] == "#":
      continue

    neighbours.append([rr, cc])
  return neighbours


q = []
q.append([sr, sc])
visited = np.zeros((R, C))
visited[sr][sc] = 1
result = []
result.append([sr, sc])
while q:
  n = []
  n = explore_neighbours(q[0][0], q[0][1])
  for i in n:
    if i[0] == er and i[1] == ec:
      print("Path found")
    if visited[i[0]][i[1]] == 0:
      visited[i[0]][i[1]] = 1
      q.append(i)
      result.append(i)
  q.pop(0)

print(visited)
print(result)
