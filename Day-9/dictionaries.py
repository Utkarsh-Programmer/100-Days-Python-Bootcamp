# making a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# retrieving items from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print()

# adding new items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
print()

# empty dictionary
empty_dictionary = {}
print(empty_dictionary)
print()

# edit an item in the existing dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])
print()

# loop through a dictionary
for i in programming_dictionary:
    print(i)  # keys
    print(programming_dictionary[i])  # values
