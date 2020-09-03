tens = {"X":10 , "XX" : 20, "XXX" : 30 , "XL" :40, "L" : 50, "LX" : 60, "LXX" : 70, "LXXX": 80, "XC" : 90}

ones = {"I": 1, "II" : 2, "III": 3, "IV" : 4, "V" : 5, "VI" : 6, "VII" : 7, "VIII" : 8, "IX":9}

int_tens = {0: "" , 1 : "X" , 2 : "XX", 3 : "XXX" , 4 : "XL", 5 : "L", 6: "LX", 7 : "LXX", 8 : "LXXX", 9 : "XC"}

int_ones = {0 : "", 1 : "I", 2 : "II", 3 : "III", 4 : "IV",5 : "V" , 6 : "VI" ,7 : "VII" ,8 : "VIII" ,9 : "IX"}

int_num = 0
done = False
str_number = input()

def is_anagram(word1, word2):
  '''
  Checks if two words are anagrams 
  param: string
  return: boolean
  '''
  
  list1 =  list(word1)
  list2 =  list(word2)
  list1.sort()
  list2.sort()
  if len(list1) != len(list2):
    return False
  for index in range(len(list1)):
    if list1[index] != list2[index]:
      return False
  return True
    
  

def num_to_roman(num):
  '''
  Converts a number into roman numeral 
  param: int
  return: string
  '''
  return int_tens[num//10] + int_ones[num%10] 

for x in range(len(str_number)-1,-1,-1):
  if str_number[0:x] in tens:
    int_num = tens[str_number[0:x]] + ones[str_number[x:len(str_number)]]
    done = True
    break

if not done:
  int_num = ones[str_number]


for x in range(1 , int_num+1):
  if is_anagram(str_number , num_to_roman(x)):
    print(num_to_roman(x))
    break
