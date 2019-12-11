#CCC '03 J1 - Trident
tine_height = int(input())
tine_space = int(input())
handle_len = int(input())

for n in range(0,tine_height):
  print("*" + " "*tine_space + "*" + " "*tine_space +"*") 

print("*" * (2*tine_space+3))

for x in range(0,handle_len):
  print(" "*(1+tine_space) + "*")
