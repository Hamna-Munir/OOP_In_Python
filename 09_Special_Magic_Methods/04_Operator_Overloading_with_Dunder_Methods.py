# ================================================================
# File: 04_Operator_Overloading_with_Dunder_Methods.py
# Topic: Operator Overloading using Dunder (Magic) Methods
# ================================================================

"""
In Python, **operator overloading** allows you to redefine how built-in operators
(like +, -, *, /, ==, <, etc.) behave for objects of your custom classes.

This is done using **dunder methods** (methods surrounded by double underscores).
For example:
    - `__add__()`  → For addition operator `+`
    - `__sub__()`  → For subtraction operator `-`
    - `__mul__()`  → For multiplication operator `*`
    - `__truediv__()` → For division operator `/`
    - `__eq__()`   → For equality operator `==`
    - `__lt__()`   → For less-than operator `<`, and so on.
"""

# ------------------------------------------------
# 1️⃣ What is Operator Overloading?
# ------------------------------------------------
"""
By default, operators like + or * work with built-in data types.

Example:
    print(10 + 5)       # Works → 15
    print("Hi" + "!")   # Works → "Hi!"

But if you try:
    obj1 + obj2
and obj1 is a custom object, Python raises an error unless you define
how + should behave for that class using __add__().
"""

# Example 1: Without operator overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2, 3)
p2 = Point(4, 5)

# print(p1 + p2)   # ❌ TypeError: unsupported operand type(s) for +: 'Point' and 'Point'


# ------------------------------------------------
# 2️⃣ Implementing __add__() for Operator Overloading
# ------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Define how + should behave
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3)  
# Output: Point(6, 8)


# ------------------------------------------------
# 3️⃣ Implementing More Operator Methods
# ------------------------------------------------
"""
You can overload almost all arithmetic and comparison operators using dunder methods.
"""

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        return ComplexNumber(
            (self.real * other.real + self.imag * other.imag) / denominator,
            (self.imag * other.real - self.real * other.imag) / denominator
        )

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Demonstrating overloaded operators
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

print("Addition:", c1 + c2)     # (3 + 7i)
print("Subtraction:", c1 - c2)  # (1 - 1i)
print("Multiplication:", c1 * c2)  # (-10 + 11i)
print("Division:", c1 / c2)        # (0.823 + -0.294i)
print("Equality:", c1 == c2)       # False


# ------------------------------------------------
# 4️⃣ Comparison Operator Overloading
# ------------------------------------------------

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __gt__(self, other):
        return self.volume > other.volume

    def __eq__(self, other):
        return self.volume == other.volume

    def __str__(self):
        return f"Box({self.volume})"

box1 = Box(10)
box2 = Box(20)
box3 = Box(10)

print(box1 < box2)  # True
print(box2 > box1)  # True
print(box1 == box3) # True


# ------------------------------------------------
# 5️⃣ Overloading __repr__() and Chaining Operations
# ------------------------------------------------
"""
To make objects print-friendly in lists and debugging,
we can also define __repr__().
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(v1 + v2)          # Vector(6, 4)
print(v1 * 3)           # Vector(6, 9)
print((v1 + v2) * 2)    # Vector(12, 8)


# ------------------------------------------------
# 6️⃣ Important Operator Overloading Methods (Reference)
# ------------------------------------------------
"""
Arithmetic Operators:
----------------------
__add__(self, other)      → +
__sub__(self, other)      → -
__mul__(self, other)      → *
__truediv__(self, other)  → /
__floordiv__(self, other) → //
__mod__(self, other)      → %
__pow__(self, other)      → **

Comparison Operators:
----------------------
__eq__(self, other) → ==
__ne__(self, other) → !=
__lt__(self, other) → <
__le__(self, other) → <=
__gt__(self, other) → >
__ge__(self, other) → >=

Unary Operators:
----------------------
__neg__(self) → -self
__pos__(self) → +self
__abs__(self) → abs(self)
"""


# ------------------------------------------------
# 7️⃣ Real-World Example — Money Class
# ------------------------------------------------

class Money:
    def __init__(self, dollars):
        self.dollars = dollars

    def __add__(self, other):
        return Money(self.dollars + other.dollars)

    def __sub__(self, other):
        return Money(self.dollars - other.dollars)

    def __eq__(self, other):
        return self.dollars == other.dollars

    def __str__(self):
        return f"${self.dollars:.2f}"

wallet1 = Money(50)
wallet2 = Money(30)
wallet3 = wallet1 + wallet2

print("Wallet 1:", wallet1)
print("Wallet 2:", wallet2)
print("Total:", wallet3)
print("Equal?", wallet1 == wallet2)


# ------------------------------------------------
# 8️⃣ Key Takeaways
# ------------------------------------------------
"""
✅ Operator overloading allows user-defined classes to behave like built-in types.
✅ Implemented using special methods like __add__, __sub__, etc.
✅ Makes objects intuitive and easy to work with.
✅ Overuse can make code confusing — use only when logically meaningful.
✅ Combine with __str__() or __repr__() for readable object representation.
"""


# ================================================================
# Summary:
# - Operator Overloading = customizing how operators work with objects.
# - Implemented using dunder methods such as __add__, __sub__, __eq__, etc.
# - Great for mathematical, data structure, and geometric object design.
# ================================================================
