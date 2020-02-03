#initializing the graph 
graph = {}
edge_list = []
while True:
  road = list(input())
  if "*" in road:
    break
  if road[0] not in graph:
    graph[road[0]] = []
  if road[1] not in graph:
    graph[road[1]] = [] 
  
  graph[road[0]].append(road[1])
  graph[road[1]].append(road[0])

  edge_list.append(road)

#initailize a bfs to see which points can reach point B 
def bfs(graph):
  '''
  Checks if point A on the graph and reach point B on the graph 
  param: graph
  return: boolean 
  '''
  #Initilaition 
  visited = {x: False for x in graph}
  q = []
  visited["A"] = True 
  q.append("A")

  while q:
    
    #pick current node
    curr_node = q.pop(0)

    if curr_node == "B":
      return True 

    #search for the next nodes 
    for adj_node in graph[curr_node]:
      if not (visited[adj_node]):
        q.append(adj_node)
        visited[adj_node] = True 


  return False



output = []
for edge in edge_list:

  #checking if this edge will cut off transportation 
  graph[edge[0]].remove(edge[1])
  graph[edge[1]].remove(edge[0])

  if not(bfs(graph)):
    output.append(edge)
  
  graph[edge[0]].append(edge[1])
  graph[edge[1]].append(edge[0])


for val in output:
  print(val[0] + val[1])

print("There are " + str(len(output)) + " disconnecting roads.")

#There are n disconnecting roads

  







