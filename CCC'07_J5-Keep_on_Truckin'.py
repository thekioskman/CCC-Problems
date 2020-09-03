mini = int(input())
maxi = int(input())

motels_added = int(input())

dp = {}

dp[0] = 1
dp[990] = 0
dp[1010] = 0
dp[1970] = 0
dp[2030] = 0
dp[2940] = 0
dp[3060] = 0
dp[3930] = 0
dp[4060] = 0
dp[4970] = 0
dp[5030] = 0
dp[5990] = 0
dp[6010] = 0
dp[7000] = 0


#0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000

for loops in range(motels_added):
  new_loc = int(input())
  dp[new_loc] = 0

dp_loc = list(dp.keys())
dp_loc.sort()

for curr_motel in dp_loc:
  for next_motels in dp_loc:
    if next_motels >= curr_motel+mini:
      if next_motels > curr_motel+maxi:
        break
      else:
        dp[next_motels] += dp[curr_motel]


print(dp[7000])
