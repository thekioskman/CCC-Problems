from sys import stdin
#input

list_val = []

num_loops = int(input())
temp = input()
for loops in range(num_loops):
  list_val.append(int(input().replace(" ",""),2))

#proccesing 

curr_row = {list_val[0]}
next_row = set()

for val in list_val[1::]:
  for num in curr_row:
    next_row.add(num^val)
  
  next_row.add(val)
  curr_row = next_row.copy()
  next_row = set()

print(len(curr_row))
