#CCC '02 S3 - Blindfold
#brute force, check every possibility for everything all for directions following instructions 
num_rows = int(input())
num_cols = int(input())

backyard = []
for loops in range(num_rows):
  line = input()
  temp_line = list(line)
  temp_line.insert(0,0)
  temp_line.insert(len(temp_line),0)
  backyard.append(temp_line)


backyard.insert(0,[0 for x in range(len(backyard[0]))])
backyard.insert(len(backyard),[0 for x in range(len(backyard[0]))])

#starting index i (1,1)

num_moves = int(input())
moves = []
for loops in range(num_moves):
  temp_move = input()
  moves.append(temp_move)

facing = ["N","E","S","W"]

def start(start_position, moves, direction):
  '''
  checks if a position is a possible starting position assuming the person starts of facing north 
  param: tuple (row,col), list , string 
  return boolean 
  '''
  global backyard , facing 
  return_list = []
  rotation = facing.index(direction) 
  row = start_position[0]
  col = start_position[1]


  for move in moves:
    if move == "R":
      rotation += 1 
    elif move == "L":
      rotation -= 1
    else:
      if facing[rotation % 4] == "N":
        row -=1 
      elif facing[rotation % 4] == "E":
        col += 1 
      elif facing[rotation % 4] == "S":
        row += 1
      elif facing[rotation % 4] == "W":
        col -= 1
    
    if backyard[row][col] == 0 or backyard[row][col] == "X":
      return_list.append(False)
      return return_list

  return_list.append(True)
  return_list.append((row,col))
  return return_list 
possible_starts = set()

for row in range(len(backyard)):
  for col in range(len(backyard[0])):
    if backyard[row][col] == "." or backyard[row][col] == "*":
      for direction in facing:
        if start((row,col),moves,direction)[0]:
          backyard[start((row,col),moves,direction)[1][0]][start((row,col),moves,direction)[1][1]] = "*"


#remove the zeros of top and bottom 
backyard.pop(0)
backyard.pop(len(backyard)-1)
temp_str = ""
for row in range(len(backyard)):
  for col in range(1,len(backyard[0])-1):
    temp_str+= backyard[row][col]
  print(temp_str)
  temp_str = ""
