line = input().split(" ")

num_moves = int(line[0])
player_health = int(line[1])
comp_health = int(line[1])


moves = []
temp = []


for loops in range(num_moves*2):
  temp_move = input().split(" ")
  temp_move[1] = int(temp_move[1])
  temp.append(temp_move)

for index in range(num_moves):
  moves.append(temp[index])
  moves.append(temp[index+num_moves])


dodge = False 
timeout = True
 
for turn in range(len(moves)):
  if turn % 2 == 0:
    
    if moves[turn][0] == "A":
      if not(dodge):
        comp_health -= moves[turn][1]
      else:
        dodge = False 
    else: #player dodges
      if dodge:
        comp_health -= moves[turn-1][1]
      else:
        dodge = True 
  else: #computer turn
    
    if moves[turn][0] == "A":
      if not(dodge):
        player_health -= moves[turn][1]
      else:
        dodge = False
    else:
      if dodge:
        player_health -= moves[turn-1][1]
      else:
        dodge = True 
  


  if player_health <= 0:
    print("DEFEAT")
    timeout = False
    break
  elif comp_health <= 0:
    print("VICTORY")
    timeout = False
    break
  else:
    continue

if timeout:
  if moves[len(moves)-1][0] == "D":
    comp_health -= moves[len(moves)-1][1]
  else:
    player_health -= moves[len(moves)-1][1]

  if comp_health <= 0:
    print("VICTORY")
  elif player_health <= 0:
    print("DEFEAT")
  else:
    print("TIE")
