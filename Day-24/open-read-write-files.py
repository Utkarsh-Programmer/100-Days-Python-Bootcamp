# opening file
# by default the files are opened in readonly mode.
file = open(file="my-text.txt")

# reading file
contents = file.read()

# printing the file content
print(contents)

# closing file
file.close()


# shortcut for opening and closing file at the same time
# opening file in writable mode
with open("new-text.txt", mode="w") as new_file:
    # older text is replaced with the new text.
    new_file.write("I've added more text to this file.")


# appending content to the file
with open("new-text.txt", mode="a") as new_file:
    # older text is replaced with the new text.
    new_file.write("I also love programming in JavaScript.")

# ------------------------------------------------------------------------------------------------------------------------------------------
# NOTE: If we try to open a file in write mode that doesn't exist, then the new file will be created.
