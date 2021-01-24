#Your life in weeks calculator

#how many days,weeks,months do you have before turning 90?

#there are 365 days, 52 weeks, 12 months in a year

age = input("What is your current age?")
int_age = int(age)

years_left = 90 - int_age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12


message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message) 
