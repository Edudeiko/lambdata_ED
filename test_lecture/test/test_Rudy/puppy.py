# Create a puppy class that takes in a name, age,
# and random weight from 10 - 50 inclusive
# Make the puppy name all upper case
# Method to show the puppies name, age, weight
# Global Puppy names
# Doc string and pep8 style guide
import random
PUPPIES = ["Pedro", "James", "Ed", "Sharma", "Zach"]


class Puppy:
    def __init__(self, name, age, weight=random.randint(10, 51)):
        self.name = name
        self.age = age
        self.weight = weight

    def make_upper(self):
        return self.name.upper()

    def show_name(self):
        print(f"The puppies name is {self.name}")

# class Leech(Puppy):
ed = Puppy("Ed", 5)

if __name__ == "__main__":
    print(ed.weight)
    print(ed.show_name())
