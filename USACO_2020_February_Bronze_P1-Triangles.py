num_posts = int(input())


cords = []

for loops in range(num_posts):
  point = input().split(" ")
  cords.append((int(point[0]), int(point[1])))


y_cords = {}
x_cords = {}


def find_common(curr_cord):
  '''
  Finds all common x and y cords and stores them in a dictionary 
  Param: tuple 
  return: list
  
  '''

  if curr_cord[0] not in x_cords:
    x_cords[curr_cord[0]] = []
    for point in cords:
      if point[0] == curr_cord[0]:
        x_cords[curr_cord[0]].append(point[1])


    #Find all common cords and store them
  
  if curr_cord[1] not in y_cords:
    y_cords[curr_cord[1]] = []
    for point in cords:
      if point[1] == curr_cord[1]:
        y_cords[curr_cord[1]].append(point[0])
  
    #Find all common cords and store them

#Store all of our common points
for points in cords:
  find_common(points)



def max_xcord(point):
  '''
  Finds the highest distance between two x cordinates
  param: integer
  return: integer
  '''
  curr_max = 0
  for val in x_cords[point[0]]:
    if abs(val-point[1]) > curr_max:
      curr_max = abs(val-point[1])
  
  return curr_max

def max_ycord(point):
  '''
  Find the highest distance between two y cordinates 
  param: integer
  return: integer
  '''
  
  curr_max = 0
  for val in y_cords[point[1]]:
    if abs(val-point[0]) > curr_max:
      curr_max = abs(val-point[0])

  return curr_max


max_area = 0 

for point in cords:
  temp = max_xcord(point) * max_ycord(point)
  if temp > max_area:
    max_area = temp
    temp = 0

print(max_area)
