# ================================================================
# File: 01_Introduction_to_Dunder_Methods.py
# Topic: Introduction to Dunder (Magic) Methods in Python
# ================================================================

"""
In Python, **Dunder Methods** (also known as **Magic Methods** or **Special Methods**) 
are predefined methods that start and end with **double underscores** (hence the name "dunder").

These methods allow you to define **how objects of a class should behave** 
with built-in operations such as printing, comparison, arithmetic, iteration, etc.

For example:
- __init__() initializes a new object.
- __str__() defines how the object is represented as a string.
- __add__() allows the use of '+' operator between objects.
"""

# ------------------------------------------------
# 1️⃣ Understanding Dunder Methods
# ------------------------------------------------

# Example: A simple class without any dunder customization

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# When we print an object of this class
s1 = Student("Hamna", 95)
print(s1)  
# Output: <__main__.Student object at 0x0000023E6A7B4D90>
# Explanation: Without __str__(), Python displays the memory location.


# ------------------------------------------------
# 2️⃣ Adding Dunder Methods to Improve Readability
# ------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(Name: {self.name}, Marks: {self.marks})"

# Now printing the object shows a human-readable message
s2 = Student("Ali", 88)
print(s2)
# Output: Student(Name: Ali, Marks: 88)


# ------------------------------------------------
# 3️⃣ Commonly Used Dunder (Magic) Methods
# ------------------------------------------------
"""
Some of the most frequently used dunder methods include:

Initialization and Representation:
----------------------------------
__init__(self, ...): Called when an object is created.
__str__(self): Defines string representation (used by print()).
__repr__(self): Defines developer-friendly representation.

Comparison Operators:
---------------------
__eq__(self, other): Defines behavior for ==
__ne__(self, other): Defines behavior for !=
__lt__(self, other): Defines behavior for <
__le__(self, other): Defines behavior for <=
__gt__(self, other): Defines behavior for >
__ge__(self, other): Defines behavior for >=

Arithmetic Operators:
---------------------
__add__(self, other): Defines +
__sub__(self, other): Defines -
__mul__(self, other): Defines *
__truediv__(self, other): Defines /
__floordiv__(self, other): Defines //

Object Lifecycle:
-----------------
__del__(self): Called when an object is deleted.
__len__(self): Defines behavior for len(object)
__call__(self): Allows objects to be called as functions.

Iteration and Containers:
-------------------------
__getitem__(self, key): Defines indexing behavior.
__setitem__(self, key, value): Defines assignment behavior.
__iter__(self): Defines iterable behavior.
__next__(self): Used with iterators.
"""


# ------------------------------------------------
# 4️⃣ Example: Demonstrating Basic Dunder Methods
# ------------------------------------------------

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book Title: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Python Basics", 250)
b2 = Book("Advanced OOP", 300)

print(b1)              # Uses __str__
print(len(b1))         # Uses __len__
print(b1 + b2)         # Uses __add__
# Output:
# Book Title: Python Basics, Pages: 250
# 250
# 550


# ------------------------------------------------
# 5️⃣ Why Use Dunder Methods?
# ------------------------------------------------
"""
Dunder methods help make your classes **behave like built-in types**.

For example:
- You can define what happens when your objects are printed, compared, added, etc.
- You can make your custom classes more intuitive and readable.
- They enable **operator overloading** and **custom object behavior**.
"""

# ------------------------------------------------
# 6️⃣ Key Points
# ------------------------------------------------
"""
✅ Dunder methods start and end with double underscores (__method__).
✅ They are automatically invoked by Python in specific situations.
✅ Common examples include __init__, __str__, __len__, and __add__.
✅ They improve readability, maintainability, and usability of custom classes.
✅ You can override them to make your objects act like built-in data types.
"""


# ================================================================
# Summary:
# Dunder (Magic) Methods → Predefined methods that allow classes to 
# integrate with Python’s built-in operations like printing, addition, 
# comparison, iteration, etc.
# ================================================================
