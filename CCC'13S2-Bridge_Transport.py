#CCC '13 S2 - Bridge Transport
max_weight = int(input())
num_trains = int(input())
trains = []
counter = 0
for loops in range(num_trains):
  temp = int(input())
  trains.append(temp)

total = 0 
#before bridge is full
stop = False 
if num_trains < 4:
  for x in range(len(trains)):
    total += trains[x]
    if total > max_weight:
      stop = True 
      break
    else:
      counter += 1
else:
  for x in range(4):
    total += trains[x]
    if total > max_weight:
      stop = True 
      break
    else:
      counter += 1





#when bridge is already full 
if not(stop):   
  for index in range(4,len(trains)):
    total -= trains[index-4]
    total += trains[index] 
    if total > max_weight:
      break
    else:
      counter += 1
  
print(counter)
