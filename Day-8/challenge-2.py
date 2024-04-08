# Challenge 2
# Caesar Cipher Part 2.

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


# encryption
def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for letter in plain_text:
        old_position = alphabet.index(letter)
        new_position = old_position+shift_amount
        new_letter = alphabet[new_position]
        encoded_text += new_letter
    print(f"The encoded text is {encoded_text}")


# ------------------------------------------------------------------------------------------------------------------------------------------


# TODO-1: Create a decrypt function called 'decrypt' that takes the 'text' and 'shift' as input.
# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
def decrypt(encrypted_text, shift_amount):
    decoded_text = ""
    for letter in encrypted_text:
        old_position = alphabet.index(letter)
        new_position = old_position-shift_amount
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print(f"The decoded text is {decoded_text}")


# TODO-3: Check if the user want to encrypt or decrypt the message checking the 'direction' variable. Then call the correct function passed on that 'direction' variable.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(encrypted_text=text, shift_amount=shift)
else:
    print("Invalid Input!")
# ------------------------------------------------------------------------------------------------------------------------------------------
