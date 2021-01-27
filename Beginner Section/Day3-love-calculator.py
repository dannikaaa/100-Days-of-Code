#create a love calculator 

#count letters against TRUE LOVE 

print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#merge both names into lowercase 
both_names = name1.lower() + name2.lower()

countT = both_names.count("t")
countR = both_names.count("r")
countU = both_names.count("u")
countE = both_names.count("e")
countL = both_names.count("l")
countO = both_names.count("o")
countV = both_names.count("v")

true = (countT + countR + countU + countE) * 10
love = countL + countO + countV + countE

total = true + love

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total <= 50 and total >= 40:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
