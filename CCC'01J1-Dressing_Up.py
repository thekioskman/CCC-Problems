#CCC '01 J1 - Dressing Up
height = int(input())
star = 1
space = height-1
for rows in range(0,height//2):
  print(star*"*" + 2*space*" " + star*"*")
  star+= 2
  space-=2



for rows in range(0,height//2+1):
  print(star*"*" + 2*space*" " + star*"*")
  star-= 2
  space+=2
