#CCC '04 S2 - TopYodeller
#Initialize variables 
temp_input = input().split(" ")
num_yodelers = int(temp_input[0])
rounds = int(temp_input[1])

ranks = {}

for key in range(1,num_yodelers+1):
  ranks[key] = []


def rank_calc(score_list):
  global ranks
  '''
  Calculates the rank of each yodeler per round 
  param: list
  return: none 
  '''
  counter = 1
  while max(score_list) > -1001:
    max_score = max(score_list)
    
    if score_list.count(max_score) > 1:
      num_ties = score_list.count(max_score)
      for x in range(num_ties):
        ranks[score_list.index(max_score) +1].append(counter)  
        score_list[score_list.index(max_score)] = -1001
      counter += num_ties  
    else:
      max_score = max(score_list)
      ranks[score_list.index(max_score) +1].append(counter)
      counter += 1
      score_list[score_list.index(max_score)] = -1001


def add_scores(list_1,list_2):
  '''
  Adds all values in a given list, given that the lists are the same length 
  param: list
  return: list
  '''
  for index in range(len(list_1)):
    list_1[index] += list_2[index]
  return list_1


prev_scores = [0 for x in range(num_yodelers)]

for loops in range(rounds):
  scores = input().split(" ")
  #Turn all vals into integers  
  for index in range(len(scores)):
    scores[index] = int(scores[index])
  
  scores = add_scores(prev_scores,scores)
  rank_calc(scores.copy())
  prev_scores = scores

winners = []
worst_rank = []

for keys in ranks.keys():
  if ranks[keys][-1] == 1:
    winners.append(keys)
    worst_rank.append(max(ranks[keys]))

for index in range(len(winners)):
  print("Yodeller",winners[index] ,"is the TopYodeller: score "+ str(scores[winners[index]-1])+", worst rank", worst_rank[index])
