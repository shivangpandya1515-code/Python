from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class: defines a common interface."""

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    """Inheritance: Dog inherits from Animal."""

    def speak(self):
        return "Dog barks"


class Cat(Animal):
    """Inheritance: Cat also inherits from Animal."""

    def speak(self):
        return "Cat meows"


# Polymorphism: different objects respond to the same method name differently
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
