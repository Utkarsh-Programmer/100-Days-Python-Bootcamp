# Exercise 2
# Prime Number Checker.

# ------------------------------------------------------------------------------------------------------------------------------------------
# WRITE YOUR CODE HERE
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")
# ------------------------------------------------------------------------------------------------------------------------------------------


# DONT'T CHANGE THE CODE BELOW
n = int(input("Check this number : "))
prime_checker(number=n)
