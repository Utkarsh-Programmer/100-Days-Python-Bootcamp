# Print is your friend.
# This code contains an error while taking 'word_per_page' input from the user. Fix the problem.

"""
pages = 0
word_per_page = 0

pages = int(input("Number of pages : "))
word_per_page == int(input("Number of words per page : "))

total_words = pages * word_per_page
print(total_words)
"""

# Solution
pages = 0
word_per_page = 0

pages = int(input("Number of pages : "))
word_per_page = int(input("Number of words per page : "))

total_words = pages * word_per_page
print(f"Pages: {pages}")
print(f"Word per page: {word_per_page}")
print(f"Total words: {total_words}")
