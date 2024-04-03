# Exercise 2
# Calculate the BMI and also give the interpretations.

# DON'T CHANGE THE CODE BELOW
height = float(input("Enter your height(m) : "))
weight = float(input("Enter your weight(Kg) : "))

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
bmi = round(weight / (height**2), 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, and you are normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, and you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, and you are obese.")
else:
    print(f"Your BMI is {bmi}, and you are clinically obese.")
# ------------------------------------------------------------------------------------------------------------------------------------------
