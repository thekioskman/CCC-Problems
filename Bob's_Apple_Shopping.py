from math import inf

line = list(map(int, input().split(" ")))

num_apples = line[1]
num_stores = line[0]

#amount = store[i-1][0]
#cost = store[i-1][1]
store = []

for loops in range(num_stores):
  store.append(tuple(map(int , input().split(" "))))


dp = [[ inf for x in range(num_apples+1)] for x in range(num_stores+1)]


for i in range(1,num_stores+1):
  for j in range(1,num_apples+1):
    if j - store[i-1][0] <= 0:
      dp[i][j] = min(dp[i-1][j] , store[i-1][1])
    else:
      dp[i][j] = min(dp[i-1][j] , dp[i][j-store[i-1][0]] + store[i-1][1])


print(dp[num_stores][num_apples])
