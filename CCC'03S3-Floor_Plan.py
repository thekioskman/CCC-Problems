flooring = int(input())
rows = int(input())
col = int(input())
visited = [ [False for x in range(25)] for x in range(25)] 
graph = []

for row in range(rows):
  line = input()
  graph.append(list(line))

rooms = []

def bfs(x, y):
  '''
  Runs bfs on a point in the graph
  param: int 
  return: int
  '''
  counter = 0
  if graph[x][y] == "I":
    return counter 
  
  elif visited[x][y]:
    return counter

  else:
    q = [(x,y)]
    visited[x][y] = True 
  
    while q:
      #count our current square as a floor we are on
      cord = q.pop(0)
      counter += 1
      #Find the next squard we can move to
      #Check all adjacent x,y values that exists in our 25*25 graph index 0-24

      #Check the two x cords 
      if 0 <= cord[0]-1 < rows:
        if not (visited[cord[0]-1][cord[1]]) and graph[cord[0]-1][cord[1]] != "I" :
          q.append( (cord[0]-1, cord[1]) )
          visited[cord[0]-1][cord[1]] = True 
      
      if 0 <= cord[0]+1 < rows:
        if not (visited[cord[0]+1][cord[1]]) and graph[cord[0]+1][cord[1]] != "I" :
          q.append( (cord[0]+1 , cord[1]) )
          visited[cord[0]+1][cord[1]] = True 
      

      #Check the two y cords 
      if 0 <= cord[1]-1 < col:
        if not (visited[cord[0]][cord[1]-1]) and graph[cord[0]][cord[1] -1] != "I" :
          q.append( (cord[0] , cord[1]-1))
          visited[cord[0]][cord[1]-1] = True 
      
      if 0 <= cord[1]+1 < col:
        if not (visited[cord[0]][cord[1]+1]) and graph[cord[0]][cord[1] +1 ] != "I" :
          q.append( (cord[0] , cord[1]+1)) 
          visited[cord[0]][cord[1]+1] = True 
    
    
    return counter
    
for x in range(rows):
  for y in range(col):
    size = bfs(x,y)
    if size:
      rooms.append(size)
      size = 0

rooms.sort(reverse = True)
counter = 0
for room in rooms:
  if flooring - room >= 0:
    counter += 1
    flooring -= room
  else:
    break 

if counter == 1:
  print(counter , "room,", flooring, "square metre(s) left over")
else:
  print(counter , "rooms,", flooring, "square metre(s) left over")
