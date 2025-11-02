"""
06_Destructor_and_Object_Lifecycle.py

This file explains destructors and the object lifecycle in Python OOP.

A destructor is a special method that is called when an object is deleted or
goes out of scope. It is mainly used for cleanup activities such as closing files,
releasing resources, or disconnecting from databases.

Topics Covered:
1. What is a Destructor
2. The __del__() Method
3. Object Lifecycle (Creation → Usage → Destruction)
4. Garbage Collection and Reference Counting
5. When Destructors are Called
6. Best Practices and Alternatives
"""

# Example 1: Basic Demonstration of Destructor
class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student object created for {self.name}")

    def __del__(self):
        print(f"Destructor called, Student object for {self.name} is being deleted")


# Object creation
s1 = Student("Hamna")
s2 = Student("Ahsan")

print("Working with Student objects...")

# Explicitly deleting one object
del s1
print("s1 object deleted manually")

# s2 will be deleted automatically when the program ends

print("\n------------------------------------------\n")


# Example 2: Object Lifecycle with Resource Management
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        print(f"Opening file: {self.filename}")
        self.file = open(filename, "w")
        self.file.write("This is a test line.\n")

    def __del__(self):
        print(f"Closing file: {self.filename}")
        self.file.close()


# Creating and using the FileManager object
manager = FileManager("example.txt")
print("File writing completed.")

# Explicitly deleting the object
del manager

print("\n------------------------------------------\n")


# Example 3: Understanding Object References and Garbage Collection
import gc


class Demo:
    def __init__(self):
        print("Demo object created.")

    def __del__(self):
        print("Destructor called for Demo object.")


# Creating multiple references to the same object
obj = Demo()
ref1 = obj
ref2 = obj
print("Multiple references to the same object created.")

# Deleting one reference
del ref1
print("Deleted ref1")

# Object not yet destroyed because other references still exist
del ref2
print("Deleted ref2")

# Now deleting last reference
del obj
print("All references deleted — object should be destroyed now.")

# Force garbage collection (for demonstration)
gc.collect()

print("\n------------------------------------------\n")


# Example 4: When Destructors Might Not Be Called Immediately
class Temp:
    def __init__(self, name):
        self.name = name
        print(f"Temp object '{self.name}' created")

    def __del__(self):
        print(f"Destructor called for Temp object '{self.name}'")


def create_temp():
    t = Temp("temporary")
    print("Exiting create_temp() function...")


create_temp()
print("After function call — Python automatically destroys local objects when no longer referenced.")

print("\n------------------------------------------\n")


# Example 5: Best Practice — Using Context Managers Instead of Destructors
class SafeFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        self.file.close()


with SafeFileHandler("safe_example.txt") as f:
    f.write("This file is managed safely using a context manager.\n")

print("File handled safely using context management.")

"""
Summary:
---------
- The destructor is defined using __del__(self)
- It is automatically invoked when the object is destroyed
- The timing of __del__ execution is managed by Python’s garbage collector
- Avoid relying solely on destructors for cleanup
- Use context managers ('with' statements) for reliable resource management
"""

