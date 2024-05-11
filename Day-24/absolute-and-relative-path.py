# NOTE: Absolute path starts from the root directory.
# Absolute File Path ==> "C:\Users\User\Documents\data.txt"

# NOTE: Relative path specifies the location of a file relative to the current working directory..
# Relative File Path ==> "../data/data.txt"


# Reading Files
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing to Files
with open("my_file.txt", mode="w") as file:
    file.write("I love programming in Python.")

# Opening a File that doesn't exit in write mode will create it from scratch
with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("This file doesn't exists.")
