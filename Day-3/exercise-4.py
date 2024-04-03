# Exercise 4
# Pizza Order.

# DONT'T CHANGE THE CODE BELOW
print("Thank's for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? s, m or l : ")
add_pepperoni = input("Do you want pepperoni? y or n : ")
extra_cheese = input("Do you want extra cheese? y or n : ")

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}.")
# ------------------------------------------------------------------------------------------------------------------------------------------
