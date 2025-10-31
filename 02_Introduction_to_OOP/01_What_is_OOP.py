# ================================================================
# Title: What is Object-Oriented Programming (OOP)?
# Description: Introduction to the concept of OOP in Python
# ================================================================


# ------------------------------------------------
# What is OOP?
# ------------------------------------------------
# Object-Oriented Programming (OOP) is a programming paradigm
# that organizes code into reusable blueprints called *classes*
# and real-world entities called *objects*.
#
# It helps structure complex programs into smaller, manageable parts.


# ------------------------------------------------
# Why OOP?
# ------------------------------------------------
# 1. Reusability – Code can be reused through inheritance.
# 2. Modularity – Code is organized into logical units (classes).
# 3. Maintainability – Easier to update and debug.
# 4. Scalability – Suitable for large, complex systems.
# 5. Data Security – Supports encapsulation and data hiding.


# ------------------------------------------------
# Core Concepts of OOP
# ------------------------------------------------
# Python supports all four pillars of OOP:
#
# 1. **Class** – A blueprint that defines attributes (data) and methods (behavior).
# 2. **Object** – An instance of a class.
# 3. **Encapsulation** – Hiding the internal state and requiring all interaction
#                       to be performed through an object’s methods.
# 4. **Inheritance** – Allows a class to derive properties and behavior from another class.
# 5. **Polymorphism** – The ability to use a single interface to represent different data types or methods.
# 6. **Abstraction** – Hiding unnecessary implementation details from the user.


# ------------------------------------------------
# Example: Without OOP (Procedural Approach)
# ------------------------------------------------
# Here we represent a car using separate functions and variables.

car_name = "Toyota"
car_color = "Red"
car_speed = 120

def start_car(name):
    return f"{name} started."

def stop_car(name):
    return f"{name} stopped."

print(start_car(car_name))
print(stop_car(car_name))


# ------------------------------------------------
# Example: With OOP (Object-Oriented Approach)
# ------------------------------------------------
# The same behavior can be modeled more cleanly using a class and objects.

class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def start(self):
        return f"{self.name} started."

    def stop(self):
        return f"{self.name} stopped."

# Creating an object of the Car class
car1 = Car("Toyota", "Red", 120)

print(car1.start())
print(car1.stop())


# ------------------------------------------------
# Summary
# ------------------------------------------------
# - OOP allows us to represent real-world entities using classes and objects.
# - It makes code more modular, maintainable, and reusable.
# - Python supports OOP fully and uses classes as the foundation of everything.
