# Modifying the global scope:

enemies = 5  # global variable
print(f"Enemies outside function {enemies}.")


def increase_enemies():
    global enemies  # make 'enemies' a global variable
    enemies += 2  # local variable
    print(f"Enemies inside function {enemies}.")


increase_enemies()
