# Multiple If statements in succession:

height = float(input("Enter your height(cm) : "))

if height > 120:
    print("You can ride the roller coster.")

    age = int(input("What's your age? "))
    if age < 12:
        ticket_price = 5
        print(f"Your ticket price is ${ticket_price}.")
    elif age > 12 and age < 18:
        ticket_price = 7
        print(f"Your ticket price is ${ticket_price}.")
    else:
        ticket_price = 12
        print(f"Your ticket price is ${ticket_price}.")

    want_photos = input("Do you want photos? ")
    if want_photos == "y":
        ticket_price += 3
        print(f"You total bill is ${ticket_price}.")
    else:
        print(f"You total bill is ${ticket_price}.")

else:
    print("You need to grow taller before riding.")
