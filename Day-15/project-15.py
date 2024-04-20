# Project 15
# Coffee Machine.

# ------------------------------------------------------------------------------------------------------------------------------------------
from menu import MENU, resources


def is_resource_sufficient(order_ingredients):
    """This function return True when order can be made and False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
        return True


def process_coins():
    """This function return the total , calculated from the coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? "))*0.1
    total += int(input("How many nickles? "))*0.05
    total += int(input("How many pennies? "))*0.01
    return total


def is_transition_successful(money_received, drink_cost):
    """This function returns True when the payment is accepted and False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """This function deduct the required ingredients from the resources and prints a message when order is completed."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# variables
is_on = True
profit = 0

# greeting
print("Welcome to the Python Coffee Machine!")

# makes program repeat
while is_on:
    # user choice
    choice = input(
        "What would you like? (espresso/latte/cappuccino):​ ").lower()

    # configuring choices
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transition_successful(money_received=payment, drink_cost=drink["cost"]):
                make_coffee(drink_name=choice,
                            order_ingredients=drink["ingredients"])

# ------------------------------------------------------------------------------------------------------------------------------------------
