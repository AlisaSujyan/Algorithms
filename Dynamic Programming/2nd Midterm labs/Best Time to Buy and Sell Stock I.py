# O(n^2)
def solution(arr):
  n = len(arr)
  buy = min(arr)
  sell = max(arr)
  if buy == sell:
    return 0
  if arr.index(buy) < arr.index(sell):
    return sell - buy, "Buy on day:", arr.index(buy), "Sell on day:", arr.index(sell)
  else:
    maximum_difference = 0
    for i in range(n):
      for j in range(i + 1, n):
        if arr[j] - arr[i] > maximum_difference:
          maximum_difference = arr[j] - arr[i]
          buy_day = i
          sell_day = j
    return maximum_difference, "Buy on day:", buy_day, "Sell on day:", sell_day


prices = [10, 15, 8, 7, 6, 9, 10, 5, 15, 20, 21, 17]
solution(prices)

prices = [4, 5, 8, 10, 6, 2, 9, 7, 1, 3, 2]
solution(prices)


# O(n)
def maximum_profit(arr):
  n = len(arr)
  profit = 0
  buy = arr[0]
  for i in range(1, n):
    if arr[i] > buy:
      profit = max(profit, arr[i] - buy)
    else:
      buy = arr[i]
  return profit

prices = [4, 5, 8, 10, 6, 2, 9, 7, 1, 3, 2]
maximum_profit(prices)