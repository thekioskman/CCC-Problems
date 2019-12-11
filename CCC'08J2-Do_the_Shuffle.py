#CCC '08 J2 - Do the Shuffle
songs = ["A","B","C","D","E"]
temp = ""
output_str = ""
while True:
  user_input = int(input())
  loops = int(input())
  if user_input == 1:
    for loops in range(loops):
      temp = songs[0]
      songs.remove(songs[0])
      songs.append(temp)
  elif user_input == 2:
    for loops in range(loops):
      temp = songs[-1]
      songs.remove(temp)
      songs.insert(0,temp)
  elif user_input == 3:
    for loops in range(loops):
      temp = songs[0]
      songs[0] = songs[1]
      songs[1] = temp
  else:
    for item in songs:
      output_str += item+" "
    print(output_str[:-1])
    break
