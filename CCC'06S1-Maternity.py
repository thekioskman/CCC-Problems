#CCC '06 S1 - Maternity
mom = input()
dad = input()
mom_allels = []
dad_allels = []
possible = True 
output = []



for index in range(0,len(mom),2):
  mom_allels.append(mom[index:index+2])

for index in range(0,len(dad),2):
  dad_allels.append(dad[index:index+2])

loops = int(input())

for loop in range(loops):
  child = input()
  for index in range(len(child)):
    if child[index].islower():
      if child[index] not in mom_allels[index] or child[index] not in dad_allels[index]:
        output.append("Not their baby!")
        possible = False 
        break
    else:
      if child[index] not in mom_allels[index] and child[index] not in dad_allels[index]:
        output.append("Not their baby!")
        possible = False 
        break
  if possible:
    output.append("Possible baby.") 
  possible = True 

for item in output:
  print(item)
