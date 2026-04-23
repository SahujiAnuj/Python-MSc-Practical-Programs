# Program 24: Multi-level Inheritance (Animal -> Mammal -> Dog)

# Base Level
class Animal:
    def eat(self):
        print("This animal eats food.")

# Level 1 - Inherits from Animal
class Mammal(Animal):
    def walk(self):
        print("This mammal walks on land.")

# Level 2 - Inherits from Mammal
class Dog(Mammal):
    def bark(self):
        print("The dog barks: Woof! Woof!")

# Level 3 - Inherits from Dog
class GuideDog(Dog):
    def help(self):
        print("This guide dog helps its owner.")

# --- Main Program ---

# Creating an object of the leaf class (GuideDog)
my_dog = GuideDog()

# Calling methods from all levels of the hierarchy
print("Testing Multi-level Inheritance:")
my_dog.eat()   # Inherited from Animal
my_dog.walk()  # Inherited from Mammal
my_dog.bark()  # Inherited from Dog
my_dog.help()  # Own method
