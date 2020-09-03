from math import inf

temp = int(input())

slimes = list(map(int , input().split(" ")))

dp = [[inf for x in range(temp)] for x in range(temp+1)]

psA = [0 for x in range(temp+1)]

for i in range(temp):
  dp[i][i] = 0 
  psA[i+1] += slimes[i] + psA[i] 


for space in range(1,temp):
  for i in range(temp-space):
    for k in range(i , i+space):
      dp[i][i+space] = min(dp[i][k] + dp[k+1][i+space] + psA[i+space+1] - psA[i] , dp[i][i+space])


print(dp[0][temp-1])
