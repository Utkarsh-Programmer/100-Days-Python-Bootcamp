# Project 8
# Caesar Cipher.

# ------------------------------------------------------------------------------------------------------------------------------------------
from logo import logo
print(logo)

# letters
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


# function to encrypt and decrypt the text.
def caesar(start_text, shift_amount, cipher_direction):
    # final result
    final_text = ""
    # when wants to decode
    if cipher_direction == "decode":
        shift_amount *= -1

    # encrypts the text byDefault
    for char in start_text:
        # when characters entered by the user are letters
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_amount
            final_text += alphabet[new_position]
        # when characters entered by the user are not letters
        else:
            final_text += char
    print(f"Here's the {cipher_direction} result: {final_text}\n")


# program is on
is_on = True

# program runs till the user wants to continue
while is_on:
    # user inputs
    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # when the shift amount entered by the user is greater than total number of alphabets
    shift %= 26

    # calling the function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # if user want to exit
    result = input(
        "\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        is_on = False
        print("Good Bye!")

# ------------------------------------------------------------------------------------------------------------------------------------------
