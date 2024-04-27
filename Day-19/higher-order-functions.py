# Higher Order Functions:
# functions that take one or more functions as argument.

def add(n1, n2):
    """Adds two number."""
    return n1+n2


def subtract(n1, n2):
    """Subtracts two number."""
    return n1-n2


def multiply(n1, n2):
    """Multiply two number."""
    return n1*n2


def divide(n1, n2):
    """Divide two number."""
    return n1/n2


# this is a higher order function.
def calculator(n1, n2, func):
    """Take to numbers and a function as input and return the result."""
    return func(n1, n2)


result = calculator(2, 3, add)
print(result)
