#create a leap year calculator 

# it is a leap yaer if it satisfies the conditions 

#    Note for leap year rules:
#        It is a leap year if it's evenly divisible by 4
#            **except** it is evenly divisible by 100
#                **unless** it is also evenly divisible by 400

#hint: draw a mindmap 

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  #it is a leap year
  
  if year % 100 == 0:
    #it is not a leap year 
    
    if year % 400 == 0:
      #it is a leap year 
      print("It is a leap year.")
    
    else:
      print("It is not a leap year.")
      
  else:
    print("It is a leap year.")

else:
  print("It is not a leap year.")
