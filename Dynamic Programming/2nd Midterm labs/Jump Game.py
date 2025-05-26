arr = [2, 4, 3, 1, 4, 5, 3, 2, 1, 5, 4, 3]

def jump(arr):
  path = []
  n = len(arr)
  if n == 1:
    return 0

  jumps = 0
  farthest = 0
  current = 0
  for i in range(n - 1):
    farthest = max(farthest, i + arr[i])

    if i == current:
      jumps += 1
      current = farthest
      path.append(arr[i])

      if current >= n - 1:
        break
  for i in range(len(path)):
    if i != len(path) - 1:
      print(path[i], end=" -> ")
    else:
      print(path[i])
  return jumps

print("Number of jumps: ", jump(arr))