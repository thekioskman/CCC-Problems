#CCC '17 J2 - Shifty Sum
num = int(input())
shifts = int(input())
total = 0
for loops in range(shifts+1):
  total += num*10**loops
print(total)
