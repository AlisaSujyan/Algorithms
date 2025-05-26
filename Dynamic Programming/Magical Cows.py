max_days = 50

# maximum number of cows
C = 8

# number of farms
N = 4

# number of visits
M = 4

dp = [[0 for i in range(C + 1)] for i in range(max_days + 1)]

initial_cows = [1, 3, 2, 1]

# all days the Regulator is coming
queries = [1, 2, 3, 4, 5, 6]

def Solve():
  for i in range(N):
    dp[0][initial_cows[i]] += 1
  for day in range(max_days):
    for i in range(C + 1):
      if i <= C/2:
        dp[day+1][2*i] += dp[day][i]
      else:
        dp[day+1][i] += 2*dp[day][i]

  print("Day 0: ", N)
  for i in range(len(queries)):
    day = queries[i]
    print(f"Day {i + 1}: ", SumRow(dp, day))
  j = 0
  for row in dp:
    print(f"day{j}", row)
    j += 1

def SumRow(dp, day):
  farms = 0
  for i in range(C+1):
    farms += dp[day][i]
  return farms

Solve()