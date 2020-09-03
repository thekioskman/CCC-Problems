max_crossers = int(input())
num_people = int(input())
dp = [] 
#The table tells us the cost to send people from 1 to i
q = []
names = []
for loops in range(num_people*2):
  line = input()
  if loops % 2 == 0:
    names.append(line)
  else:
    q.append(int(line))


#initialize dp 
total_time = 0
for person in q:
  total_time += person
  dp.append(total_time)

dp.append(0)#Hotfix: appended 0 to the end of the list because we had to grab dp[-1] which we wanted to be zero, since we had not initialized the dp to 0 

#initialize prev array 
#We set the value of each prev to the index of the one before it, 
#It appears as if they crossed alone
prev = [-1] * num_people


for i in range(len(q)):
  for j in range(0,max_crossers):
    if i+j >= len(q): #cannot assumes that we can end our interation at len(q) - max_crosses, becuase we might need to form group sizes less that max_crossers. 
      break
    elif max(q[i:i+j+1]) + dp[i-1] < dp[i+j]:
      prev[i+j] = i-1
    #make sure to check the case of i = 0 becuase then we are grabing dp[-1]
    dp[i+j] = min(dp[i+j], max(q[i:i+j+1])+ dp[i-1])
   
curr = num_people-1
groups = []
while curr >= 0:
  groups.append(names[prev[curr]+1: curr+1])
  curr = prev[curr]






print("Total Time:", dp[num_people-1])

for group in groups[::-1]:
  temp_str = ""
  for people in group:
    temp_str += people+" "
  print(temp_str)
