# ================================================
# File: 02_Function_and_Operator_Overloading.py
# Topic: Function and Operator Overloading in Python
# ================================================

"""
In Object-Oriented Programming, **overloading** refers to using the same name
for multiple functions or operators that behave differently depending on 
their input.

Python supports:
1. **Function Overloading (limited)** — Same function name with different behavior.
2. **Operator Overloading** — Defining how operators (+, -, *, /, etc.) behave for custom objects.
"""

# ------------------------------------------------
# 1️⃣ FUNCTION OVERLOADING
# ------------------------------------------------
"""
In some programming languages (like C++ or Java), you can define multiple 
functions with the same name but different parameter lists.

Python does **not** support true function overloading directly.
Instead, it allows **default arguments** or **variable-length arguments** to 
simulate function overloading.
"""

print("----- Example 1: Function Overloading using Default Arguments -----")

def greet(name=None):
    if name is not None:
        print(f"Hello, {name}!")
    else:
        print("Hello, User!")

greet()           # Output: Hello, User!
greet("Hamna")    # Output: Hello, Hamna!


print("\n----- Example 2: Function Overloading using *args -----")

def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(5, 10))            # Output: 15
print(add(5, 10, 15))        # Output: 30
print(add(1, 2, 3, 4, 5))    # Output: 15


print("\n----- Example 3: Function Overloading with Type Checking -----")

def multiply(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)     # Concatenation for strings
    else:
        return a * b               # Multiplication for numbers

print(multiply(3, 4))       # Output: 12
print(multiply("Hi", 3))    # Output: HiHiHi
print(multiply("Hamna", "Ali"))  # Output: HamnaAli


# ------------------------------------------------
# 2️⃣ OPERATOR OVERLOADING
# ------------------------------------------------
"""
Operators like +, -, *, /, ==, etc., have predefined meanings for built-in types.
But in Python, you can redefine how these operators behave for your **user-defined classes**.

This is done by overriding **special methods** (also called **magic methods**) 
such as:
- __add__() for +
- __sub__() for -
- __mul__() for *
- __truediv__() for /
- __eq__() for ==
- __lt__() for <
- __gt__() for >
"""

print("\n===============================================")
print("        OPERATOR OVERLOADING EXAMPLES          ")
print("===============================================")


# ------------------------------------------------
# 3️⃣ Example: Overloading '+' Operator
# ------------------------------------------------
print("\n----- Example 4: Overloading '+' Operator -----")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student("Hamna", 85)
s2 = Student("Ali", 90)

print("Total Marks:", s1 + s2)   # Output: 175


# ------------------------------------------------
# 4️⃣ Example: Overloading Multiple Operators
# ------------------------------------------------
print("\n----- Example 5: Overloading +, -, * Operators -----")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("Addition:", v1 + v2)     # Output: Vector(6, 8)
print("Subtraction:", v1 - v2)  # Output: Vector(-2, -2)
print("Multiplication:", v1 * v2)  # Output: Vector(8, 15)


# ------------------------------------------------
# 5️⃣ Example: Overloading Comparison Operators
# ------------------------------------------------
print("\n----- Example 6: Overloading Comparison Operators -----")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

e1 = Employee("Hamna", 60000)
e2 = Employee("Ali", 55000)
e3 = Employee("Sara", 60000)

print("Is e1 salary greater than e2?", e1 > e2)   # True
print("Do e1 and e3 have equal salary?", e1 == e3) # True


# ------------------------------------------------
# 6️⃣ Example: Overloading __str__ for String Representation
# ------------------------------------------------
print("\n----- Example 7: Overloading __str__ Method -----")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

book1 = Book("Python Basics", "Hamna", 250)
book2 = Book("AI with Python", "Ali", 300)

print(book1)
print(book2)


# ------------------------------------------------
# 7️⃣ Summary of Common Magic Methods
# ------------------------------------------------
"""
Commonly used magic methods for operator overloading:
-----------------------------------------------------
__add__(self, other)        → x + y
__sub__(self, other)        → x - y
__mul__(self, other)        → x * y
__truediv__(self, other)    → x / y
__floordiv__(self, other)   → x // y
__mod__(self, other)        → x % y
__pow__(self, other)        → x ** y
__eq__(self, other)         → x == y
__ne__(self, other)         → x != y
__lt__(self, other)         → x < y
__le__(self, other)         → x <= y
__gt__(self, other)         → x > y
__ge__(self, other)         → x >= y
__str__(self)               → str(x)
__repr__(self)              → repr(x)
"""


# ------------------------------------------------
# 8️⃣ Advantages of Overloading
# ------------------------------------------------
"""
✅ Increases code readability and expressiveness.
✅ Enables intuitive use of operators on user-defined objects.
✅ Provides flexibility to define object behavior.
✅ Makes code cleaner and closer to natural language.
"""


# ================================================
# Summary:
# - Python does not support true function overloading, but can simulate it using default or variable arguments.
# - Operator overloading allows user-defined classes to redefine how operators behave.
# - Done using special (magic) methods like __add__, __sub__, __eq__, etc.
# - Overloading improves code clarity, reusability, and OOP design.
# ================================================
