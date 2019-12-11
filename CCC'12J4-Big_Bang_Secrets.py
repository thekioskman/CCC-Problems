#CCC '12 J4 - Big Bang Secrets
k = int(input())
code = input()
temp_str = ""
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_dict = {}
counter = 1
for char in alpha:
  alpha_dict[char] = counter
  counter += 1
counter = 1
alpha = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in code:
  index = (alpha_dict[char] - 3*counter) - k 
  if index <= 0:
    index += 26 
  temp_str += alpha[index]
  counter += 1
print(temp_str)
