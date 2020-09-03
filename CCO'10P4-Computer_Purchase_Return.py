num_type = int(input())

num_parts = int(input())

parts = {x: [] for x in range(1, num_type+1)}

for loops in range(num_parts):
  line = list(map(int, input().split(" ")))
  parts[line[2]].append(line[0:2])

budget = int(input())

dp = [[0 for x in range(budget+1)] for x in range(num_type+1)]

counter = 0
for i in range(1, num_type+1):
  for j in range(budget+1):
    for item in parts[i]:
      if j - item[0] < 0:
        dp[i][j] = max(dp[i][j] , 0)
        counter += 1
      else:
        dp[i][j] = max(dp[i][j] , dp[i-1][j-item[0]] + item[1])
  if counter == len(parts[i]):
    print(-1)
    break
  counter = 0

print(dp[num_type][budget])
