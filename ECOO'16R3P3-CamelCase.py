from math import inf
num_words = int(input())

words = set()
for loops in range(num_words):
  line = input()
  words.add(line)


for loops in range(10):
  
  word = input()

  dp = [inf for x in range(len(word) +1)]
  dp[-1] = 0

  j = len(word)

  for j in range(len(word) , -1 , -1):
    for i in range(j , -1 , -1):
      if word[i:j] in words:
        dp[i] = min(dp[i] , dp[j]+1)
  
  print(dp[0] -1)
