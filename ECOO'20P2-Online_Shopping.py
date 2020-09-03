num_cases = int(input())
output = []
def bin_search( name , price , num_item):
  '''
  inserts the item based in the correct order based on price
  param: string, int, int
  return: none
  '''
  list_1 = dic[name]
  skip = False
  if price < list_1[0][0]:
    dic[name] = [(price, num_item)] + dic[name]
    skip = True
  if not(skip):
    start = 0
    end = len(list_1)
    mid = (start+end)//2
    while start+1 != end:
      mid = (start+end)//2
      if list_1[mid][0] > price:
        end = mid
      else:
        start = mid
    
    if price > list_1[mid][0]:
      dic[name] = list_1[0: mid+1] + [(price, num_item)] + list_1[mid+1::]
    else:
      dic[name] = list_1[0:mid] + [(price, num_item)] + list_1[mid::]


for loops in range(num_cases):
  dic = {}

  num_store = int(input())

  #getting all the items into the stores list
  for loops in range(num_store):
    num_items = int(input())

    for items in range(num_items):
      line = input().split(" ")
      if line[0] not in dic:
        dic[line[0]] = [(int(line[1]) , int(line[2]))]
      else:
        bin_search(line[0] , int(line[1]) , int(line[2]))


  items_buy = int(input())
  total = 0
  for loops in range(items_buy):
    line = input().split(" ")
    items_left = int(line[1])
    for items in dic[line[0]]:
      if items_left <= items[1]:
        total += items[0]*items_left
        break
      else:
        total += items[0] * items[1]
        items_left -= items[1]
  
  output.append(total)

for val in output:
  print(val)
