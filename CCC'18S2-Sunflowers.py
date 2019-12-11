#CCC '18 J4/S2 - Sunflowers
chart = []
temp_list = []
x = int(input())

def splice_by_space(string):
  '''
  Given a string input, it spices the string based on blank spaces
  param: String 
  return: list
  
  '''
  temp_str = ""
  return_list = []
  for char in string:
    if char == " ":
      return_list.append(int(temp_str))
      temp_str = ""
    else:
      temp_str+= char
  return_list.append(int(temp_str))

  return return_list

for loops in range(0,x):
  data = input()
  chart.append(splice_by_space(data))

#Data is organized into a 2D array, dont know how to procces it tho? 

def left_rotation(list_1,n):
  '''
  given a 2D array it rotates it 90 left 
  param: 2d array 
  return: 2d array
  '''

  new_list = []
  temp_list = []
  for x in range(n-1,-1,-1):
    for y in range(n):
      temp_list.append(list_1[y][x])

    new_list.append(temp_list)
    temp_list = []

  return new_list

while not(chart[0][0] < chart[0][1] and chart[0][0] < chart[1][0]):
  chart = left_rotation(chart,x)

temp_str = ""

for row in range(x):
  for col in range(x):
    temp_str += str(chart[row][col]) + " "
  print(temp_str)
  temp_str = ""
