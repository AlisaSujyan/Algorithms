def target_sum(arr, target):
  total_sum = sum(arr)

  if target > total_sum or (target + total_sum) % 2 == 1:
    return False

  subset_sum = (target + total_sum) // 2
  dp = [0 for i in range(subset_sum + 1)]
  dp[0] = 1

  for num in arr:
    for i in range(subset_sum, num - 1, -1):
      dp[i] += dp[i - num]

  return dp[subset_sum]

print("The number of different expressions: ", target_sum([1, 1, 1, 1, 1], 3))