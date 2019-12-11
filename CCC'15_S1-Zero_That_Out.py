#CCC '15 S1 - Zero That Out
loops = int(input())
list_1 = []

for loops in range(loops):
  num = int(input())
  if num == 0:
    list_1.pop(-1)
  else:
    list_1.append(num)

total = 0 

for items in list_1:
  total += items 

print(total)
