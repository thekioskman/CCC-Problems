temp = int(input())

nums = list(map(int , input().split(" ")))

dp = [[0 for x in range(temp)] for x in range(temp+1)]

psA = [0]
total = 0
for val in nums:
  total += val
  psA.append(total)



for space in range(temp):
  for i in range(temp-space):
    dp[i][i+space] = max((psA[i+space+1] - psA[i]) - dp[i+1][i+space] ,(psA[i+space+1] - psA[i]) - dp[i][i+space-1] )


print(dp[0][temp-1] - (psA[-1] -dp[0][temp-1]) )
