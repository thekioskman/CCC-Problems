#CCC '05 J3 - Returning Home
directions = ["HOME"]
line = ""
while line != "SCHOOL":
  line = input()
  directions.append(line)

for index in range(len(directions)-2,0,-2):
  if directions[index] == "R":
    if directions[index-1] == "HOME":
      print("Turn LEFT into your HOME.")
      break
    else:
      print("Turn LEFT onto", directions[index-1], "street.")
  else:
    if directions[index-1] == "HOME":
      print("Turn RIGHT into your HOME.")
      break 
    else:
      print("Turn RIGHT onto", directions[index-1] ,"street.")
