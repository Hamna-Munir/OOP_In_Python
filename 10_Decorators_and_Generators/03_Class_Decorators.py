# ================================================================
# File: 03_Class_Decorators.py
# Topic: Class Decorators in Python
# ================================================================

"""
In Python, decorators are not limited to functions — they can also be applied to **classes**.

A **class decorator** is a function that takes a class as input, modifies or extends its
behavior, and returns the modified class.

👉 In short:
    Function decorators → Modify or extend function behavior.
    Class decorators    → Modify or extend class behavior.

They are useful for:
    - Automatically registering classes
    - Adding attributes or methods
    - Enforcing constraints
    - Logging or debugging
    - Implementing design patterns like Singleton
"""

# ------------------------------------------------
# 1️⃣ Basic Example of a Class Decorator
# ------------------------------------------------
"""
A simple decorator that adds a new attribute to the class.
"""

def add_author_info(cls):
    cls.author = "Hamna - OOP In Python Repository"
    return cls

@add_author_info
class ExampleClass:
    pass

print(ExampleClass.author)
# Output: Hamna - OOP In Python Repository


# ------------------------------------------------
# 2️⃣ Class Decorator Adding a Method Dynamically
# ------------------------------------------------
"""
Class decorators can also add methods dynamically.
"""

def add_greet_method(cls):
    def greet(self):
        return f"Hello! I am a dynamically added method in {cls.__name__}."
    cls.greet = greet
    return cls

@add_greet_method
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Touseef")
print(student.greet())  # Output: Hello! I am a dynamically added method in Student.


# ------------------------------------------------
# 3️⃣ Class Decorator for Logging Object Creation
# ------------------------------------------------
"""
A class decorator that logs when an instance is created.
"""

def log_object_creation(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"[LOG] Creating instance of {cls.__name__} with arguments {args}, {kwargs}")
        original_init(self, *args, **kwargs)
    cls.__init__ = new_init
    return cls

@log_object_creation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

acc = BankAccount("Hareem", 5000)
# Output: [LOG] Creating instance of BankAccount with arguments ('Hareem', 5000), {}


# ------------------------------------------------
# 4️⃣ Class Decorator for Validating Attributes
# ------------------------------------------------
"""
This decorator enforces that all numeric fields must be positive.
"""

def validate_positive_values(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for key, value in self.__dict__.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"[ERROR] {key} cannot be negative!")
    cls.__init__ = new_init
    return cls

@validate_positive_values
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

p1 = Product("Laptop", 80000, 5)
print(p1.__dict__)

# Uncomment to see error:
# p2 = Product("Phone", -20000, 3)
# Raises ValueError: [ERROR] price cannot be negative!


# ------------------------------------------------
# 5️⃣ Singleton Pattern Using a Class Decorator
# ------------------------------------------------
"""
A Singleton ensures that only one instance of a class can exist.

We can implement it easily with a class decorator.
"""

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            print(f"[INFO] New instance of {cls.__name__} created.")
        else:
            print(f"[INFO] Existing instance of {cls.__name__} returned.")
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected to Database"

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True


# ------------------------------------------------
# 6️⃣ Automatic Class Registration Example
# ------------------------------------------------
"""
This pattern automatically registers classes in a global dictionary.
Useful for plugin systems or frameworks.
"""

registry = {}

def register_class(cls):
    registry[cls.__name__] = cls
    print(f"[REGISTERED] {cls.__name__} added to registry.")
    return cls

@register_class
class Teacher:
    pass

@register_class
class Course:
    pass

print("Registered Classes:", registry)
# Output:
# [REGISTERED] Teacher added to registry.
# [REGISTERED] Course added to registry.
# Registered Classes: {'Teacher': <class '__main__.Teacher'>, 'Course': <class '__main__.Course'>}


# ------------------------------------------------
# 7️⃣ Applying Multiple Class Decorators
# ------------------------------------------------
"""
Like function decorators, multiple class decorators can be chained.
They are applied from bottom to top.
"""

def decorator_one(cls):
    print("Decorator One Applied")
    return cls

def decorator_two(cls):
    print("Decorator Two Applied")
    return cls

@decorator_one
@decorator_two
class MultiDecorated:
    pass

# Output:
# Decorator Two Applied
# Decorator One Applied


# ------------------------------------------------
# 8️⃣ Real-World Example — Adding a Timestamp
# ------------------------------------------------
"""
This decorator adds a creation timestamp attribute to every class instance.
"""

import datetime

def add_timestamp(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.created_at = datetime.datetime.now()
    cls.__init__ = new_init
    return cls

@add_timestamp
class Employee:
    def __init__(self, name):
        self.name = name

emp = Employee("Arslan")
print(emp.name, "created at:", emp.created_at)


# ------------------------------------------------
# 9️⃣ Using functools.wraps with Class Decorators
# ------------------------------------------------
"""
Although functools.wraps is mostly used for function decorators,
you can still use it to preserve metadata in decorator-generated functions.
"""

from functools import wraps

def preserve_metadata(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        print(f"Creating {cls.__name__} object...")
        return cls(*args, **kwargs)
    return wrapper

@preserve_metadata
class Vehicle:
    """Represents a vehicle with brand information."""
    def __init__(self, brand):
        self.brand = brand

v = Vehicle("Toyota")
print(Vehicle.__name__)  # Vehicle
print(Vehicle.__doc__)   # Represents a vehicle with brand information.


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ Class decorators take a class, modify it, and return it.
✅ They can:
   - Add attributes or methods
   - Log object creation
   - Enforce constraints
   - Implement design patterns (e.g., Singleton)
   - Automatically register classes
✅ You can apply multiple decorators to a class.
✅ Same @decorator syntax applies for functions and classes.
✅ Best Practice: Keep class decorators simple and well-documented.
"""


# ================================================================
# Summary:
# Class Decorators → Modify or extend class behavior dynamically.
# Common Uses → Logging, validation, registration, Singleton, metadata injection.
# Syntax → @decorator_name above class definition.
# ================================================================
