# CCC '01 S1 - Keeping Score
cards = input()
#in the master list the first list repersent clubs then diamonds, hearts,spades
master_list = [[],[],[],[]]
# card id is the suit of the card, 0 = clubs, 1 = diamonds, ect
card_id = 0 
for card in cards:
  if card == "D":
    card_id = 1
  elif card == "H":
    card_id = 2
  elif card == "S":
    card_id = 3
  else:
    master_list[card_id].append(card)

master_list[0].remove("C")

#point tally for clubs 
c_points = 0 
points = 3 - len(master_list[0])
if  points > 0:
  c_points += points 
for card in master_list[0]:
  if card == "A":
    c_points += 4
  elif card == "K":
    c_points += 3 
  elif card == "Q":
    c_points += 2
  elif card == "J":
    c_points += 1
  else:
    c_points += 0


  
#Point tally for diamonds 
d_points = 0 
points = 3 - len(master_list[1])
if  points > 0:
  d_points += points 
for card in master_list[1]:
  if card == "A":
    d_points += 4
  elif card == "K":
    d_points += 3 
  elif card == "Q":
    d_points += 2
  elif card == "J":
    d_points += 1
  else:
    d_points += 0




#tally for hearts 
h_points = 0 
points = 3 - len(master_list[2])
if  points > 0:
  h_points += points 
for card in master_list[2]:
  if card == "A":
    h_points += 4
  elif card == "K":
    h_points += 3 
  elif card == "Q":
    h_points += 2
  elif card == "J":
    h_points += 1
  else:
    h_points += 0




#tally for spades 
s_points = 0 
points = 3 - len(master_list[3])
if  points > 0:
  s_points += points 
for card in master_list[3]:
  if card == "A":
    s_points += 4
  elif card == "K":
    s_points += 3 
  elif card == "Q":
    s_points += 2
  elif card == "J":
    s_points += 1
  else:
    s_points += 0




#formating
clubs = ""
diamonds = ""
hearts = ""
spades = ""

for cards in master_list[0]:
  clubs += (cards+" ")

for cards in master_list[1]:
  diamonds += (cards+" ")
  
for cards in master_list[2]:
  hearts += (cards+" ")
  
for cards in master_list[3]:
  spades += (cards+" ")

total = c_points +d_points+h_points+s_points
print("Cards Dealt          Points")
print("Clubs"+" "+clubs+"          " + str(c_points))
print("Diamonds"+" "+diamonds+"          " + str(d_points))
print("Hearts"+" "+hearts+"          " + str(h_points))
print("Spades"+" "+spades+"          " + str(s_points))
print("Total   "+ str(total))
