output = []

while True:

  nums = list(map(int , input().split(" ")))
  temp = len(nums)
  if temp == 1:
    break
  

  dp = [[0 for x in range(temp)] for x in range(temp)]

  for space in range(2, temp):
    for i in range(temp-space):
      for k in range(i+1 , i+space):
        dp[i][i+space] = max(dp[i][i+space] , nums[i] + nums[k] + nums[i+space] + dp[i][k] + dp[k][i+space])
  
  output.append(dp[1][temp-1])

for val in output:
  print(val)
