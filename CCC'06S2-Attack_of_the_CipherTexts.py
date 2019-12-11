#CCC '06 S2 - Attack of the CipherTexts
plain_txt = input()
cipher1 = input()
cipher2 = input()

list_plain = list(plain_txt)
list_cipher1 = list(cipher1)
decoder = {}
for index in range(len(list_plain)):
  decoder[list_cipher1[index]] = list_plain[index]

temp_str = ""

for char in cipher2:
  if char not in decoder.keys():
    temp_str += "."
  else:
    temp_str += decoder[char]

print(temp_str)
