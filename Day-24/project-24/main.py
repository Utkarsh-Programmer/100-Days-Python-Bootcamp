# Project 24
# Mail Merge Project.

# NOTE: readlines() method is used to read all lines from a file and return them as a list of strings.
# NOTE: replace() method is used to create a new string by replacing all occurrences of a specified substring with another substring.
# NOTE: strip() method is used to remove leading and trailing characters (whitespace characters by default) from a string.

# ------------------------------------------------------------------------------------------------------------------------------------------
PLACEHOLDER = "[name]"


# Reading names and storing in list.
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


# Reading the letter text.
with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter_contents = letters_file.read()

    # Stripping names and replacing them with the "[name]" placeholder.
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Making completed letter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
# ------------------------------------------------------------------------------------------------------------------------------------------
