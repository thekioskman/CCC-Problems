from math import inf
line = input().split(" ")
graph = {x:[] for x in range(1 , int(line[0]) +1 )}
for loops in range(int(line[1])):
  user_input = input().split(" ")
  graph[int(user_input[0])] += [( int(user_input[1]), int(user_input[2]) )]
  graph[int(user_input[1])] += [( int(user_input[0]), int(user_input[2]) )]


def djk(graph, start):
  '''
  finds the shortest paths from the start to every point in the graph
  param: dict, int
  return: none 
  '''

  visited = [False] * (len(graph)+1)
  dist = [inf] * (len(graph)+1) 
  visited[start] = True 
  dist[start] = 0 
  curr_node = start
  for loops in range(int(line[0])):

    for adj_node in graph[curr_node]:
      if not(visited[adj_node[0]]):
        if adj_node[1] + dist[curr_node] < dist[adj_node[0]]:
          dist[adj_node[0]] = adj_node[1] + dist[curr_node]

    temp_min = inf
    for node in range(1,len(graph)+1):
      if not(visited[node]):
        if dist[node] < temp_min:
          temp_min = dist[node]
          curr_node = node
    
    
    if temp_min == inf:
      break
    else:
      visited[curr_node] = True 
  
  for x in dist[1:]:
    if x == inf:
      print(-1)
    else:
      print(x)

djk(graph,1)
