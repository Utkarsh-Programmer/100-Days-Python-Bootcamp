# Nested If and Elif statement:

height = int(input("Enter your height? "))

if height > 120:
    print("You can ride the roller coster.")
    age = int(input("What's your age? "))
    if age < 12:
        print("You ticket price is $5.")
    elif age > 12 and age < 18:
        print("Your ticket price is $7.")
    else:
        print("Your ticket price is $12.")
else:
    print("You need to grow taller before riding.")
