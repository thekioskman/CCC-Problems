line = input().split(" ")
total_time = int(line[0])
t = int(line[1])

up = int(line[2])
flat = int(line[3])
down = int(line[4])

terrain = list(input())


counter = 0
while total_time > 0:
  if terrain[counter] == "f":
    total_time -= 2*flat
  else:
    total_time -= down
    total_time -= up 
  counter += 1

print(counter-1)
