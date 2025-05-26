items = 5
capacity = 7

dict = {'1': [2, 3],
        '2': [2, 1],
        '3': [4, 3],
        '4': [5, 4],
        '5': [3, 2]}

dp = [[0 for i in range(capacity + 1)] for i in range(items + 1)]

def solve(dp, items, capacity, dict):
  for i in range(1, items + 1):
    for key, value in dict.items():
      if key == str(i):
        j = value[1]
        dp[i][0:value[1]] = dp[i - 1][0:value[1]]
        while j <= capacity:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-value[1]] + value[0])
          j += 1
  return dp

result = solve(dp, items, capacity, dict)

counter = -1
for row in result:
  counter += 1
  print(f"Item{counter}", row)

picked_items = []
j = capacity
for i in range(items, 0, -1):
    if dp[i][j] != dp[i - 1][j]:
      picked_items.append(i)
      j -= dict[str(i)][1]

print("Picked items:", picked_items)