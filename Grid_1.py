line = list(map(int , input().split(" ")))
num_row = line[0]
num_col = line[1]

dp = [[ 0 for x in range(num_col)] for x in range(num_row)]

dp[0][0] = 1
line = input()

for col in range(1,num_col):
  if line[col] == ".":
    dp[0][col] = dp[0][col-1]
  else:
    dp[0][col] = 0

for row in range(1,num_row):
  line = input()
  for col in range(num_col):
    if line[col] == ".":
      dp[row][col] = dp[row-1][col] + dp[row][col-1]
    else:
      dp[row][col] = 0

print(dp[row][col] % (10**9+7))
