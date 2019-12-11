#CCC '16 J4 - Arrival Time
depart = input()
#XX:XX

mins = int(depart[3::])
hours = int(depart[0:2])


#if leave at 5:20 spend 20 mins in rush hour trafic, has to calculate that 
def rush_hour(hour, mins):
  '''
  Checks if the time is in rush hour 
  param: integer
  return: boolean 
  '''


  if hour >= 15 and hour < 19:
    return True 
  elif hour >= 7 and hour < 10:
    return True 
  else:
    return False 
counter = 120 
while counter > 0:
  if rush_hour(hours, mins):
    counter-= 1 
    mins += 2 
    hours += mins//60
    mins = mins%60 
  else:
    counter -= 1
    mins += 1 
    hours += mins//60
    mins = mins%60 

if hours >= 24:
  hours %= 24




    
print("%.2d:%.2d" % (hours ,mins ))
