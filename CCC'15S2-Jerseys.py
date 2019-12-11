#CCC '15 S2 - Jerseys
list_jerseys = [0]
num_jerseys = int(input())
num_althetes = int(input())
counter = 0 

for loops in range(num_jerseys):
  jersey = input()
  list_jerseys.append(jersey)

def req(string):
  '''
  seperates the jersey size the athlete requires and the number they want, puts it into list 
  param: string 
  return: list
  '''
  return_list = string.split(" ")
  return_list[1] = int(return_list[1])
  return return_list


for athletes in range(num_althetes):
  temp = input()
  athlete_req = req(temp)

  if list_jerseys[athlete_req[1]] <= athlete_req[0]:
    counter += 1 
    list_jerseys[athlete_req[1]] = "z"

print(counter)
