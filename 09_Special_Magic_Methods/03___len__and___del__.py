# ================================================================
# File: 03___len__and___del__.py
# Topic: The __len__() and __del__() Dunder Methods in Python
# ================================================================

"""
Python provides several **dunder (magic) methods** that allow you to define
how objects of a class behave with built-in functions and operations.

Two important such methods are:
1. **__len__()**  → Defines the behavior of the `len()` function.
2. **__del__()**  → Defines what happens when an object is deleted.
"""

# ------------------------------------------------
# 1️⃣ The __len__() Method
# ------------------------------------------------
"""
Definition:
------------
The **__len__()** method is used to define how the built-in `len()` function 
should behave for objects of a class.

When you call `len(object)`, Python internally executes:
    object.__len__()

Purpose:
---------
- Allows you to specify a “length” property for custom objects.
- Commonly used in data structures, collections, or classes that hold multiple items.
"""

# Example 1: Using __len__() in a simple class

class BookCollection:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

collection = BookCollection(["Python Basics", "OOP in Python", "Data Structures"])
print(len(collection))  
# Output: 3


# Example 2: A class where len() returns a calculated value

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __len__(self):
        return len(self.songs)

my_playlist = Playlist("Favorites", ["Song1", "Song2", "Song3", "Song4"])
print(f"Playlist '{my_playlist.name}' has {len(my_playlist)} songs.")
# Output: Playlist 'Favorites' has 4 songs.


# ------------------------------------------------
# 2️⃣ The __del__() Method
# ------------------------------------------------
"""
Definition:
------------
The **__del__()** method is called **when an object is about to be destroyed**.
It is also known as the **destructor** in Python.

Purpose:
---------
- Used to perform cleanup operations (like closing files, releasing memory, etc.).
- Called automatically when the object’s reference count reaches zero.

Syntax:
--------
    def __del__(self):
        # cleanup code
"""

# Example 3: Demonstrating __del__()

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        print(f"Opening file: {self.filename}")

    def __del__(self):
        print(f"Closing file: {self.filename}")

# Object creation and deletion
f1 = FileHandler("data.txt")
del f1
# Output:
# Opening file: data.txt
# Closing file: data.txt


# Example 4: Automatic call to __del__() when object goes out of scope

class Temp:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

def create_object():
    t = Temp()

create_object()
# Output:
# Object created
# Object destroyed


# ------------------------------------------------
# 3️⃣ Combining __len__() and __del__() in One Class
# ------------------------------------------------

class ShoppingCart:
    def __init__(self):
        self.items = []
        print("Shopping cart created!")

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def __len__(self):
        return len(self.items)

    def __del__(self):
        print("Shopping cart is now deleted. Thank you for shopping!")

cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Headphones")

print("Items in cart:", len(cart))
del cart

# Output:
# Shopping cart created!
# Added: Laptop
# Added: Headphones
# Items in cart: 2
# Shopping cart is now deleted. Thank you for shopping!


# ------------------------------------------------
# 4️⃣ Important Notes on __del__()
# ------------------------------------------------
"""
⚠️ The __del__() method should be used carefully.

- It is called automatically when the object is **garbage collected**.
- However, the **timing** of garbage collection in Python is not guaranteed.
- You should not rely on __del__() for critical operations like saving data to a file.
- Instead, use `with` statements or explicit close() methods for cleanup.
"""

# Example 5: Why timing is uncertain
import time

class Demo:
    def __del__(self):
        print("Destructor called")

obj = Demo()
print("Deleting object reference...")
obj = None   # Hint for garbage collection
time.sleep(1)
print("End of program")
# Output order may vary depending on when garbage collector runs.


# ------------------------------------------------
# 5️⃣ Key Points
# ------------------------------------------------
"""
✅ __len__() defines the behavior of len(object).
✅ __del__() defines the cleanup behavior when an object is destroyed.
✅ __del__() may not execute immediately — timing depends on garbage collection.
✅ Use __len__() to represent collection size or logical length of an object.
✅ Avoid using __del__() for critical operations; prefer context managers instead.
"""


# ================================================================
# Summary:
# - __len__() → Customizes the behavior of the len() function.
# - __del__() → Acts as a destructor to handle cleanup when objects are deleted.
# Together, they make classes more functional and memory-aware.
# ================================================================
