# Reproduce the bug.
# Sometimes the program will run and sometime shows IndexError. Fix this problem.

""" 
from random import randint
dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
"""


# Solution
from random import randint
dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
