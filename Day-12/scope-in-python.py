# Local Scope and Global Scope:

# global variable
player_health = 10


def drink_potion():
    # local variable
    potion_strength = 2
    print(potion_strength)
    print(player_health)


drink_potion()
# print(potion_strength) # Name error
