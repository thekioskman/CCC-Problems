#CCC '07 S2 - Boxes
loops = int(input())
boxes = []
output = []
box_fit = False 

def fits(item,box):
  '''
  Given dimensions of an item checks if it fits in a box of given dimensions 
  param: list 
  return: list
  '''
  for checks in range(3):
    if max(item) > max(box):
      return False 
    else:
      item.remove(max(item))
      box.remove(max(box))
  return True 

def vol(box):
  '''
  With given dimensions, calculates the volume 
  param: list
  return: Integer
  '''
  total = 1
  for dim in box:
    total *= dim 
  return total 

for loop in range(loops):
  dimen = input()
  boxes.append(dimen.split(" "))

for row in range(len(boxes)):
  for col in range(3):
    boxes[row][col] = int(boxes[row][col])

#oder boxes smallest to biggest 
for loops in range(len(boxes)):
  for box in range(len(boxes)-1):
    if vol(boxes[box]) > vol(boxes[box+1]):
      temp = boxes[box]
      boxes[box] = boxes[box+1]
      boxes[box+1] = temp


num_items = int(input())

for loops in range(num_items):
  dimen = input()
  item = dimen.split(" ")
  for index in range(3):
    item[index] = int(item[index])

  for box in boxes:
    if fits(item.copy(),box.copy()):
      output.append(vol(box))
      box_fit = True 
      break 
    else:
      continue   
  
  if not(box_fit):
    output.append("Item does not fit.")
  box_fit = False 

for item in output:
  print(item)
