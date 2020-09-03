from math import inf

seq = input()
temp = len(seq)


dp = [[0 for x in range(temp)] for x in range(temp)]

dic = {"[":"]",  "(":")" }

#initialize dp

for i in range(temp):
  dp[i][i] = 1

for counter in range(1,temp):
  for i in range(temp-counter):
    if seq[i] in dic and seq[i+counter] == dic[seq[i]]:
      
      min_val = dp[i+1][i+counter-1]
      for k in range(i , i+counter):
        min_val =  min(dp[i][k] + dp[k+1][i+counter], min_val)
      
      dp[i][i+counter] = min_val
    else:
      min_val = inf
      for k in range(i , i+counter):
        min_val =  min(dp[i][k] + dp[k+1][i+counter], min_val)
      
      dp[i][i+counter] = min_val



print(dp[0][temp-1])
