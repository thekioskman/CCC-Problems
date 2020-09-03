import collections

line = list(map(int,input().split(" ")))
dic = {}
for loops in range(line[0]):
  user_input = list(map(int,input().split(" ")))
  if user_input[0] not in dic:
    dic[user_input[0]] = user_input[1]
  else:
    dic[user_input[0]] += user_input[1]

price = 0
boxes_left = line[1]
dic2 = dict(collections.OrderedDict(sorted(dic.items())))
for key in dic2:
  if dic[key] < boxes_left:
    boxes_left -= dic2[key]
    price += dic2[key] * key
  else:
    price += boxes_left * key
    break
    
print(price)
