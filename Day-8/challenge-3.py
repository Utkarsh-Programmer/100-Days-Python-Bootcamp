# Challenge 3
# Caesar Cipher Part 3.

# letters
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# user inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# ------------------------------------------------------------------------------------------------------------------------------------------
# function to encrypt and decrypt the text.
def caesar(start_text, shift_amount, cipher_direction):
    # final result
    final_text = ""
    # when wants to decode
    if cipher_direction == "decode":
        shift_amount *= -1

    # encrypts the text byDefault
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position+shift_amount
        final_text += alphabet[new_position]
    print(f"Here's the {cipher_direction} result: {final_text}")


# calling the function
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
# ------------------------------------------------------------------------------------------------------------------------------------------
