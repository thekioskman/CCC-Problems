#CCC '00 J3 - Slot Machines
money = int(input())
first_played = int(input())
sec_played = int(input())
third_played = int(input())

num_plays = 0 
while money > 0:
  #machine one
  if money > 0:
    first_played += 1 
    money -= 1
    num_plays += 1
    if first_played == 35:
      money += 30 
      first_played = 0

  else:
    break 
  #machine two 
  if money > 0:
    sec_played += 1 
    money -= 1
    num_plays += 1
    if sec_played == 100:
      money += 60 # pays one quater to play, so net gain is 59 not 60 (NOT COPRRECT ASUMPTION TO MAKE)
      sec_played = 0
  
      
      
  else:
    break 
  #machine three
  if money > 0:
    third_played += 1 #first change(put this infront)
    money -= 1
    num_plays += 1
    if third_played == 10:
      money += 9 
      third_played = 0 
    
      
      
  else:
    break 

print("Martha plays"+" "+str(num_plays)+" "+ "times before going broke.")
