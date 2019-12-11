#CCC '00 S4 - Golf
dist = int(input())
dp = {}
clubs = []
num_clubs = int(input())

for loops in range(num_clubs):
  temp = int(input())
  clubs.append(temp)

for keys in range(dist+1):
  dp[keys] = dist+1

dp[0] = 0


for dis in dp.keys():
  for club in clubs:
    if dis >= club:
      dp[dis] = min(dp[dis], dp[dis - club] + 1)


if dp[dist] != dist+1:
  print("Roberta wins in", dp[dist] ,"strokes.")
else:
  print("Roberta acknowledges defeat.")
