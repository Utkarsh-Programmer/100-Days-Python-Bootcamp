# Positional Arguments:
def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What it's like in {location}.")


greet_with_name("Billie", "Nowhere")
greet_with_name("Nowhere", "Billie")
print()


# Keyword arguments:
def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What it's like in {location}.")


greet_with_name(name="Billie", location="Nowhere")
greet_with_name(location="Billie", name="Nowhere")
