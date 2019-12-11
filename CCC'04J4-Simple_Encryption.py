#CCC '04 J4 - Simple Encryption
key_word = input()

word = input()

new_alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alpha = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}


def isalpha(char):
  '''
  Checks if char is alpha
  param: string 
  return boolean 
  '''
  string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return char in string 

list_1 = list(filter(isalpha, word))


counter = 0 
for index in range(len(list_1)):
  if counter == len(key_word):
    counter = 0
  
  list_1[index] = new_alpha[(alpha[key_word[counter]] + alpha[list_1[index]])%26] 
  counter += 1



temp_str = ""
for char in list_1:
  temp_str += char 

print(temp_str)
