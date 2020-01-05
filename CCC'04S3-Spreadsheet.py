graph = []

for rows in range(10):
  line = input().split(" ")
  graph.append(["0"] + line) #So we dont have to do index-1 

convert = {"A":0, "B":1 , "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}



#Finds all cycles in the spreadsheet

def cycles_dsf(letter, str_num):
  '''
  Checks the each node in the graph and sees if it creates a cycles with itself by running dfs on the node   
  '''
  original = letter+str_num
  x = convert[letter]
  y = int(str_num)
  if graph[x][y].isnumeric():
    return False 
  else:
    #Iniatlization 
    visited = [[False for x in range(10)] for x in range(10)]
    q = graph[x][y].split("+") 

    visited[x][y] = True 

    #Proccesing 
    while q:
      curr_node = q.pop(0)
      
      if curr_node == original:
        return False

      adj_nodes = graph[convert[curr_node[0]]][int(curr_node[1])]

      if not(adj_nodes.isnumeric()): 
        
        for adj_node in adj_nodes.split("+"):
          if adj_node == original:
            return True 
          elif adj_node == "*":
            return False
          else:
            if not(visited[convert[adj_node[0]]][int(adj_node[1])]):
              q.append(adj_node)
              visited[convert[adj_node[0]]][int(adj_node[1])] = True
    return False   


for char in convert:
  for num in range(10):
    if cycles_dsf(char, str(num)):
      graph[convert[char]][num] = "*"
  

#Runs a bfs to computer the values for each cell 
def bfs(x, y):
  '''
  Runs bfs on every cord in the graph 
  '''
  counter = 0
  #Base Casses 
  if graph[x][y].isnumeric():
    return graph[x][y]
  elif graph[x][y] == "*":
    return "*"
  
  else:
    #Initialization 
    #dont need visited becuase we dont be stuck in loops 
    q = graph[x][y].split("+")
    total = 0
    
    #Proccessing 
    while q:
      counter += 1
      curr_node = q.pop(0)  

      
      if graph[convert[curr_node[0]]][int(curr_node[1])].isnumeric(): #Check our next node, if our next node is a number
          
          total += int(graph[convert[curr_node[0]]][int(curr_node[1])]) 
      
      else:
        #If our next node is more directions 
          
        adj_nodes = graph[convert[curr_node[0]]][int(curr_node[1])]
        
        if adj_nodes.isnumeric():
          total += int(adj_nodes)
        else:
          for adj_node in adj_nodes.split("+"):
            if adj_node == "*":
              return "*"
            else:
              q.append(adj_node)

    return str(total)


for x in range(10):
  for y in range(10):
    graph[x][y] = bfs(x,y)



for row in graph:
  temp_str = ""
  for char in row[1:]:
    temp_str += char +" "
  
  print(temp_str)
