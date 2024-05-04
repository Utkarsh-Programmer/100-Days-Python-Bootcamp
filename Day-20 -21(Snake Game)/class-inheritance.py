# Class inheritance:

class Animal:
    """This class is a super class for the 'Fish' class."""

    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    """This class contains a super class named 'Animal'."""

    def __init__(self):
        # access all attributes and methods of its super class.
        super().__init__()

    def breathe(self):
        # access 'breathe' method only from the super class.
        super().breathe()
        print("Breathing under water")

    def swim(self):
        print("Swimming in water.")


nemo = Fish()
nemo.swim()

# using methods from super class.
nemo.breathe()

# using attributes from super class.
print(nemo.eyes)
