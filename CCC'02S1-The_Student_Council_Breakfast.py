#CCC '02 S1 - The Students' Council Breakfast
pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
total = int(input())
min_counter = 30
counter = 0 
for pink_mul in range(total//pink+1):
  for green_mul in range(total//green+1):
    for red_mul in range(total//red+1):
      for orange_mul in range(total//orange+1):  
        if pink_mul*pink + green_mul*green + red_mul*red + orange_mul*orange == total:
          print("# of PINK is", pink_mul, "# of GREEN is", green_mul, "# of RED is", red_mul, "# of ORANGE is",orange_mul)
          counter += 1
          temp_counter = pink_mul + green_mul + red_mul + orange_mul
          if temp_counter < min_counter:
            min_counter = temp_counter 
            temp_counter = 0 

print("Total combinations is",str(counter)+".")




    
  
  
  

print("Minimum number of tickets to print is", str(min_counter)+".")
