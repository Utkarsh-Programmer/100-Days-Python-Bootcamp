# Exercise 5
# Love Calculator.

# DON'T CHANGE THE CODE BELOW
print("The Love Calculator is calculating your score...")
name1 = input("What's your name? ")
name2 = input("What's their name? ")

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
# .lower() method is used to lower case the string.
combined_names = (name1+name2).lower()

# .count() method counts for a specified character in a specified string.
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

true = t+r+u+e
love = l+o+v+e

love_score = str(true)+str(love)
int_love_score = int(love_score)

if int_love_score < 10 or int_love_score > 90:
    print(
        f"Your love score is {int_love_score}, you go together like coke and mentos.")
elif int_love_score >= 40 and int_love_score <= 50:
    print(f"Your love score is {int_love_score}, you are alright together.")
else:
    print(f"Your love score is {int_love_score}.")
# ------------------------------------------------------------------------------------------------------------------------------------------
