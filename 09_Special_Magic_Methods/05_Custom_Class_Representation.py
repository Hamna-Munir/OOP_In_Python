# ================================================================
# File: 05_Custom_Class_Representation.py
# Topic: Custom Class Representation using __str__() and __repr__()
# ================================================================

"""
When working with objects in Python, it's often important to control how those
objects are **represented** — both for users (human-readable) and for developers (debugging).

Python provides two special dunder (double underscore) methods for this:
    1. __str__()  → User-friendly string representation.
    2. __repr__() → Developer-friendly string representation (for debugging).
"""

# ------------------------------------------------
# 1️⃣ The Need for Custom Class Representation
# ------------------------------------------------
"""
By default, if you print an object of a user-defined class, Python shows something like:

    <__main__.Person object at 0x000002A3...>

This output shows the memory address of the object, which is not helpful.
To make the object more readable or useful, we can customize its representation
using __str__() and __repr__().
"""

# Example without __str__ or __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p)  # Output: <__main__.Person object at ...>


# ------------------------------------------------
# 2️⃣ Using __str__() for Readable Representation
# ------------------------------------------------
"""
__str__() defines the **human-readable** string shown when you call print() on an object.
It should return a clear, user-oriented message.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 25)
print(p)  # Output: Alice, 25 years old


# ------------------------------------------------
# 3️⃣ Using __repr__() for Developer-Friendly Representation
# ------------------------------------------------
"""
__repr__() defines the **official string representation** of an object.

It is used:
    - In the Python shell (REPL)
    - Inside lists, dictionaries, or debugging tools
    - When print() is not explicitly used but the object is displayed

Goal: __repr__() should, ideally, return a string that could be used to recreate the object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Bob", 30)
print(p)        # Output: Person(name='Bob', age=30)
print([p])      # Output: [Person(name='Bob', age=30)]


# ------------------------------------------------
# 4️⃣ Difference Between __str__() and __repr__()
# ------------------------------------------------
"""
- __str__() is for users → readable and friendly.
- __repr__() is for developers → unambiguous and often resembles valid Python code.

If both are defined:
    - print(obj) → calls __str__()
    - directly typing obj in interpreter → calls __repr__()

If only __repr__() is defined, Python uses it as a fallback for both.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

    def __str__(self):
        return f"{self.name} — ${self.price}"

item = Product("Laptop", 1200)
print(item)       # Uses __str__() → Laptop — $1200
print([item])     # Uses __repr__() → [Product(name='Laptop', price=1200)]


# ------------------------------------------------
# 5️⃣ When to Use Each
# ------------------------------------------------
"""
✅ Use __str__():
   - When you want a pretty, user-readable output.
   - Example: displaying in UI, logs, or print statements.

✅ Use __repr__():
   - When debugging or developing.
   - Should ideally help recreate the object (eval-safe when possible).
"""

# Example: Both methods defined clearly
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

b = Book("1984", "George Orwell", 1949)
print(b)        # Uses __str__()
print(repr(b))  # Uses __repr__()
print([b])      # Also uses __repr__()


# ------------------------------------------------
# 6️⃣ Practical Example — Custom Representation in a Data Class
# ------------------------------------------------
"""
Custom representations are very helpful in debugging or logging complex data structures.
"""

class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def __repr__(self):
        return f"Employee(emp_id={self.emp_id}, name='{self.name}', position='{self.position}')"

    def __str__(self):
        return f"{self.name} ({self.position})"

e1 = Employee(101, "Tauseef", "Software Engineer")
e2 = Employee(102, "Hareem", "Data Analyst")

print(e1)       # Tauseef (Software Engineer)
print([e1, e2]) # [Employee(emp_id=101, name='Tauseef', position='Software Engineer'), Employee(emp_id=102, name='Hareem', position='Data Analyst')]


# ------------------------------------------------
# 7️⃣ __repr__() Best Practice
# ------------------------------------------------
"""
✅ __repr__() should aim to be an unambiguous representation of the object.
✅ Should return a string that could theoretically be used to recreate it.
✅ It helps debugging tools and logs show clear and complete information.
"""


# ------------------------------------------------
# 8️⃣ If You Don’t Define Either
# ------------------------------------------------
"""
If neither __str__() nor __repr__() are defined:
    Python will display a generic memory reference like:
    <__main__.ClassName object at 0x000002...>
"""


# ------------------------------------------------
# 9️⃣ Shortcut: Using dataclasses for automatic __repr__
# ------------------------------------------------
"""
The `dataclasses` module (Python 3.7+) can automatically generate __repr__() for you.
"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: int
    major: str

s = Student("Zain", 112668, "Software Engineering")
print(s)
# Output: Student(name='Zain', roll_no=112668, major='Software Engineering')


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ __str__()  → readable, user-facing representation (used by print()).
✅ __repr__() → detailed, developer/debugging representation.
✅ If __str__() is missing, __repr__() is used as fallback.
✅ dataclasses automatically generate __repr__() for convenience.
✅ Use both together for professional, clear object outputs.
"""


# ================================================================
# Summary:
# - __str__() → readable text for end users
# - __repr__() → technical text for debugging
# - Both enhance clarity and debugging in OOP design.
# ================================================================
