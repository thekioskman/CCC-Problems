#CCC '01 J2 - Mod Inverse
num_1 = int(input())
num_2 = int(input())
exists = False 
for nums in range(1,num_2):
  if (num_1 * nums) % num_2 == 1:
    print(nums)
    exists = True 


if not(exists):
  print("No such integer exists.")
