line_length = int(input())

str_a = input()
str_b = input()
counter = 0

curr_mode = True #Everytime this changed from true to false, we add 1 to the counter

for index in range(line_length):
  if curr_mode:
    if str_a[index] != str_b[index]:
      counter += 1
      curr_mode = False
  else:
    if str_a[index] == str_b[index]:
      curr_mode = True


print(counter)
