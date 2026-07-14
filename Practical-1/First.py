# Python OOP: Classes, Objects, Attributes and Methods
# Objective: Implement and understand Python OOP concepts.

class Student:
    def __init__(self, name, age):
        self.name = name      # Attribute
        self.age = age        # Attribute

    def display_info(self):  # Method
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def is_adult(self):      # Method
        return self.age >= 18


# Creating objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 16)

# Accessing attributes and calling methods
student1.display_info()
print(f"Is {student1.name} an adult? {student1.is_adult()}")

student2.display_info()
print(f"Is {student2.name} an adult? {student2.is_adult()}")