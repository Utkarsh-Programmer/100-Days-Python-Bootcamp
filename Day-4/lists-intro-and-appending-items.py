# Lists are used to store collections of items and are ordered and mutable.

states_of_america = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]

print(states_of_america)
print()

# number of items in list
print(len(states_of_america))

# accessing list by index position
print(states_of_america[0])
print(states_of_america[-1])

# changing list items
states_of_america[2] = "Hogwarts"
print(states_of_america[2])

# appending items to the end of list
states_of_america.append("Mist Kingdom")
print(states_of_america[-1])

# adding multiple items to the end of list
states_of_america.extend(["CLover Kingdom", "Ice Kingdom"])
print(states_of_america[-1])
print(states_of_america[-2])
print()

print(states_of_america)
