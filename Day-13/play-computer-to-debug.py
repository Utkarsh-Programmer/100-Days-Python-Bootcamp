# Play Computer to Debug.
# This code doesn't work if the year is 1994. Fix this problem.

""" 
year = int(input("What's your year of birth : "))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
"""

# Solution
year = int(input("What's your year of birth : "))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")
