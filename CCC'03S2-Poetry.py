#CCC '03 S2 - Poetry
stanzas = int(input())
vowels = set(["a","e","i","o","u"])

def ryhme(string1, string2):
  '''
  Checks if two words rhyme
  param: string 
  return: boolean 
  '''
  for index in range(len(string1)-1, 0,-1):
    if string1[index] in vowels:
      string1 = string1[index::]
      break
  for index in range(len(string2)-1, 0,-1):
    if string2[index] in vowels:
      string2 = string2[index::]
      break
  if string1 == string2:
    return True 
  else:
    return False 


print_list = []
last_words = [0]
for stanza in range(stanzas):
  
  for lines in range(4):
    line = input()
    line = line.lower()
    temp_list = line.split(" ")
    if not(temp_list[-1].isalpha()):
      last_words.append(temp_list[-2])
    else:
      last_words.append(temp_list[-1])
  
  if ryhme(last_words[1],last_words[2]) and ryhme(last_words[3],last_words[4]) and ryhme(last_words[1],last_words[3]):
    print_list.append("perfect")
  
  elif ryhme(last_words[1],last_words[2]) and ryhme(last_words[3],last_words[4]):
    print_list.append("even")
  
  elif ryhme(last_words[1],last_words[3]) and ryhme(last_words[2],last_words[4]):
    print_list.append("cross")
  
  elif ryhme(last_words[1],last_words[4]) and ryhme(last_words[2],last_words[3]):
    print_list.append("shell")
  
  else:
    print_list.append("free")
  
  last_words = [0]

for item in print_list:
  print(item)
