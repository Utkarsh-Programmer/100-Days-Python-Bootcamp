# Project 2
# Tip Calculator.

# ------------------------------------------------------------------------------------------------------------------------------------------
# greeting
print("Welcome to the Tip Calculator!")

# total bill
bill = float(input("What was the total bill? "))

# tip percent
tip = int(input("How much tip would you like to give? "))

# number of people
people = int(input("How many people to split the bill? "))

# tip amount from the bill
tip_amount = (bill * tip) / 100

# bill with tip
bill_with_tip = bill + tip_amount

# bill per person
bill_per_person = bill_with_tip / people

# final print statement
print(f"Each person should pay ${round(bill_per_person, 2)}")
# ------------------------------------------------------------------------------------------------------------------------------------------
