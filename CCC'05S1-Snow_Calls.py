#CCC '05 S1 - Snow Calls
converter = {}
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter = 0
value = 2
stopper = True 
for key in alpha:
  converter[key] = value 
  counter += 1
  if counter % 3 == 0:
    value += 1

converter["S"] = 7
converter["V"] = 8
converter["Y"] = 9
converter["Z"] = 9
counter = 0
num_numbs = int(input())
temp = []
output = []
for loops in range(num_numbs):
  temp = []
  counter = 0
  stopper = True 
  line = input()
  line = list(line)
  for char in line:
    if char != "-": 
      if char.isalpha():
        temp.append(converter[char])
      else:
        temp.append(char)
      counter += 1 
      if counter % 3 == 0 and stopper:
        temp.append("-")
      if counter == 6:
        stopper = False 
    
    
    if len(temp) == 12:
      break 
  output.append(temp)
temp_str = ""
for number in output:
  temp_str = ""
  for char in number:
    temp_str += str(char)
  print(temp_str)
