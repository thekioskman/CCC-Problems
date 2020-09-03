from math import inf
num_cows = int(input())
data = []
for loops in range(num_cows):
  line = list(map(int , input().split(" ")))
  data.append(line)

data.sort(key = lambda x : x[0])

data.append([inf,0]) #dummy variable at end



def infec_rad(data):
  '''
  Find the infection radius 
  input: list
  return: int
  '''
  return_val = inf
  for index in range(len(data)-1):
    if data[index][1] == 0:
      if data[index+1][1] == 1:
        return_val = min(data[index+1][0] - data[index][0], return_val )
      if data[index-1][1] == 1:
        return_val = min(data[index][0] - data[index-1][0], return_val )

  return return_val


rad = infec_rad(data)
counter = 0
unique = True
for index in range(len(data)-1):
  if data[index][1] == 1:
    if unique:
      counter += 1
    if data[index+1][0] - data[index][0]< rad:
      unique = False 
    else:
      unique = True 

print(counter)
