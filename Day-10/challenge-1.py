# Challenge 1
# Calculator Part 1.

# ------------------------------------------------------------------------------------------------------------------------------------------
# add
def add(num1, num2):
    return num1+num2


# subtract
def subtract(num1, num2):
    return num1-num2


# multiply
def multiply(num1, num2):
    return num1*num2


# divide
def divide(num1, num2):
    return num1/num2


# available operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# number inputs
num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

# display the available options
for operation in operations:
    print(operation)

# operation input
operation_symbol = input("Pick an operation from the above : ")

# answer
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

# final output
print(f"{num1} {operation_symbol} {num2} = {answer}")
# ------------------------------------------------------------------------------------------------------------------------------------------
