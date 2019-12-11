#CCC '19 S2 - Pretty Average Primes
num_test = int(input())
prime_set = {2,3}
def isPrime(num):
  '''
  Checks if a number is prime
  '''
  if num in prime_set:
    return True 
  for factors in range(3,int(num**.5)+1,2):
    if num % factors == 0:
      return False 
  prime_set.add(num)
  return True 
for loops in range(num_test):
  num = int(input())
  num *= 2 
 
  
  
  
  for nums in range(5,num,2):
    if isPrime(nums):
      if isPrime(num-nums):
        print(nums,num-nums)
        break
