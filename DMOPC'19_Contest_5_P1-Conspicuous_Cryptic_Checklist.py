line = input().split(" ")
num_items = int(line[0])

num_tasks = int(line[1])

counter = num_tasks
items = set()

for loops in range(num_items):
  thing = input()
  items.add(thing)


for loops in range(num_tasks):

  reps = int(input())
  temp_list = []
  for loops in range(reps):
    item = input()
    temp_list.append(item)
  
  for thing in temp_list:
    if thing not in items:
      counter -= 1
      break
  

print(counter)
