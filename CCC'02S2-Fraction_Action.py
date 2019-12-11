#CCC '02 S2 - Fraction Action
num = int(input())
denom = int(input())

def reduce_frac(num,denom):
  '''
  Reduces the fraction to its simplest form 
  '''
  for factors in range(2,denom):
    while num % factors == 0 and denom % factors == 0:
      num //= factors 
      denom//=factors 
  
  return [num,denom]


if num % denom == 0:
  print(num// denom)
elif num // denom == 0:
  print(str(reduce_frac(num%denom,denom)[0])+"/" + str(reduce_frac(num,denom)[1]))
else:
  print(num//denom, str(reduce_frac(num%denom,denom)[0])+"/" + str(reduce_frac(num,denom)[1]))
