#Create a BMI Calculator

#BMI forumula 
#bmi = weight/height**2

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#find out the type of height & weight 
#print(type(height))
#print(type(weight))

#change the types into int & float
int_weight = int(weight)
float_height = float(height)

#change bmi type as well
bmi = int_weight/float_height**2
int_bmi = int(bmi)
print(int_bmi)
