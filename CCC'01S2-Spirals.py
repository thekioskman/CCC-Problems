#CCC '01 S2 - Spirals 
start_num = int(input())
end_num = int(input())
list_1 = [[0]*100 for rows in range(100)]
row = len(list_1)//2
col = len(list_1[0])//2
step = 1 
end = False 
down = True 
right = True 
up = True 
num = (start_num+1) 
list_1[row][col] = start_num

while num <= end_num:
  if down and not(end):
    #we are moving down on the grid
    down = False
    for moves in range(step):
      row += 1
      list_1[row][col] = num  
      num+=1 
      if num > end_num:
        end = True 
        break 
  
  
  elif right and not(end):
    #we are moving right 
  
    for moves in range(step):
      col += 1 
      list_1[row][col] = num 
      num+=1  
      if num > end_num:
        end = True 
        break
    #update step and direction 
    step += 1
    right = False
  
  elif up and not(end):
    #we are moving up 
    
    for moves in range(step):
      row -= 1 
      list_1[row][col] = num 
      num+=1 
      if num > end_num:
        end = True 
        break 
    up = False 
 
  elif not(end):
    #this makes it go left, we reset all of our direction value 
    #we are going left 
    for moves in range(step):
      col -= 1
      list_1[row][col] = num 
      num+=1  
      if num > end_num:
        end = True
        break
    step += 1 
    down = True 
    right = True 
    up = True  



#Figure out how to output 

#Find dimensions of the grid i need to print


def start_row(list_1):
  '''
  Find the first row where there is a non zero number
  param: list
  return: int
  '''
  for row in range(len(list_1)):
    for col in range(len(list_1[0])):
      if list_1[row][col] != 0:
        return row
def end_row(list_1):
  '''
  Find the last row where there is a non zero number
  param: list
  return: int
  '''
  for row in range(len(list_1)-1,0,-1):
    for col in range(len(list_1[0])):
      if list_1[row][col] != 0:
        return row 
def start_col(list_1):
  '''
  Find the first col where there is a non zero number
  param: list
  return: int
  '''
  for col in range(len(list_1[0])):
    for row in range(len(list_1)):
      if list_1[row][col] != 0:
        return col 

def end_col(list_1):
  '''
  Finds the last colum where ther is a non-zero number
  param: list
  return: int
  '''
  for col in range(len(list_1[0])-1,0,-1):
    for row in range(len(list_1)):
      if list_1[row][col] != 0:
        return col 

startr = start_row(list_1)
endr = end_row(list_1)
startc = start_col(list_1)
endc = end_col(list_1)
temp_str = ""
for row in range(startr,endr+1):
  for col in range(startc,endc+1):
    if list_1[row][col] == 0:
      temp_str += "   "
    else:
      temp_str += "%2d "% list_1[row][col]
  print(temp_str)
  temp_str = ""


