#CCC '02 J2 - AmeriCanadian
vowels = {"a","e","i","o","u","y"}
def wordChange(word):
  '''
  Checks if a word uses american spelling 
  param: String 
  return: String 
  '''
  if len(word) > 4:
    if word[-2:] == "or":
      if word[word.find("or")-1] not in vowels:
        word = word[:word.find("or")] +"our"+ word[word.find("or")+2:]
        return word
      else:
        return word
    else:
      return word 
  else:
    return word 
while True: 
  word = input()
  if word == "quit!":
    break 
  else:
    print(wordChange(word))
