#a tip calculator 

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))

tip = float(input("What percentage tip would you like to give? "))

people = int(input("How many people to split the bill? "))

tip_percent = tip/100
tip_amt = tip_percent * bill 
total_bill = tip_amt + bill 
bill_per_person = total_bill/people

final_amt = round(bill_per_person, 2) #but it does not show the extra zero 
final_amt = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amt}.")
