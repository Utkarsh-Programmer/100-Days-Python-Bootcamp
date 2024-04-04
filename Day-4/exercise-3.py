# Exercise 3
# Treasure Map.

# DON'T CHANGE THE CODE BELOW
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]

print("Hiding your Treasure! X marks the spot.")

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
location = input("Enter the location to hide the Treasure : ")

letter = location[0].lower()
number = int(location[1])

letters = ["a", "b", "c"]

# .index() method is used to find the first occurrence of the specified value.
letter_position = letters.index(letter)
number_position = number-1

map[number_position][letter_position] = "X"
# ------------------------------------------------------------------------------------------------------------------------------------------

# DON'T CHANGE THE CODE BELOW
print(f"\n{line1} \n{line2} \n{line3}")
