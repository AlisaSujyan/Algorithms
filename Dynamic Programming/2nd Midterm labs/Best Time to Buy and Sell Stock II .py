def maximum_profit(arr):
  n = len(arr)
  profit = 0
  for i in range(1, n):
    if arr[i] > arr[i - 1]:
      profit += arr[i] - arr[i - 1]
  return profit

prices = [10, 15, 8, 7, 6, 9, 10, 5, 15, 20, 21, 17]
print(maximum_profit(prices))