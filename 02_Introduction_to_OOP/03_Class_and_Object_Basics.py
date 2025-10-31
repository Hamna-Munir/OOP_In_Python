# ================================================================
# Title: Class and Object Basics in Python
# Description: Understanding how to define and use classes and objects
# ================================================================


# ------------------------------------------------
# What is a Class?
# ------------------------------------------------
# A class is a blueprint or template for creating objects.
# It defines the structure and behavior (data and methods) of objects.
#
# ➤ Think of a class as a plan or design.
# ➤ It does not occupy memory until an object is created from it.
#
# Syntax:
# class ClassName:
#     # attributes and methods


# ------------------------------------------------
# What is an Object?
# ------------------------------------------------
# An object is an instance of a class.
# When an object is created, memory is allocated for it.
#
# ➤ Objects represent real-world entities.
# ➤ Each object can have its own unique data (attributes).


# ------------------------------------------------
# Example 1: Creating a Simple Class and Object
# ------------------------------------------------

class Student:
    # Class attribute
    college_name = "AI & ML Institute"

    # Instance method
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age        # Instance variable

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, College: {Student.college_name}")

# Creating objects
student1 = Student("Hamna", 22)
student2 = Student("Ali", 21)

# Accessing object methods
student1.show_info()
student2.show_info()

# Output:
# Name: Hamna, Age: 22, College: AI & ML Institute
# Name: Ali, Age: 21, College: AI & ML Institute


# ------------------------------------------------
# Accessing Attributes
# ------------------------------------------------
# You can access instance and class attributes using the dot (.) operator.

print(student1.name)          # Output: Hamna
print(Student.college_name)   # Output: AI & ML Institute


# ------------------------------------------------
# Modifying Attributes
# ------------------------------------------------
# You can modify instance and class attributes separately.

student1.name = "Hamna Munir"       # modifies only this object
Student.college_name = "ML Academy" # modifies class-level attribute (affects all objects)

student1.show_info()
student2.show_info()
# Output:
# Name: Hamna Munir, Age: 22, College: ML Academy
# Name: Ali, Age: 21, College: ML Academy


# ------------------------------------------------
# Example 2: Multiple Objects with Different Attributes
# ------------------------------------------------

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating multiple objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display()
car2.display()
# Output:
# Car Brand: Toyota, Model: Corolla
# Car Brand: Honda, Model: Civic


# ------------------------------------------------
# The 'self' Parameter
# ------------------------------------------------
# - Refers to the current object (instance) of the class.
# - Used to access instance variables and methods.
# - Must be the first parameter in every instance method definition.
#
# Example:

class Example:
    def display(self):
        print("This is called using the object reference!")

obj = Example()
obj.display()  # Output: This is called using the object reference!


# ------------------------------------------------
# Summary
# ------------------------------------------------
# - A class is a blueprint; an object is an instance of that blueprint.
# - Use the __init__() method to initialize object attributes.
# - 'self' refers to the current instance of the class.
# - Class attributes are shared across all objects, while instance attributes are unique per object.
# - Classes help structure code and represent real-world entities more effectively.
