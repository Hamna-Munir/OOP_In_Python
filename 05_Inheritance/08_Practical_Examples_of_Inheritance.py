# ================================================
# File: 08_Practical_Examples_of_Inheritance.py
# Topic: Practical Examples of Inheritance in Python
# ================================================

"""
Inheritance is one of the core concepts of Object-Oriented Programming (OOP).
It allows one class (child/subclass) to acquire the properties and behaviors
of another class (parent/superclass).

In this file, we will explore **real-world, practical examples** of inheritance
to understand how it improves code organization, reusability, and extensibility.
"""

# ------------------------------------------------
# 1️⃣ Example: Employee Management System
# ------------------------------------------------
# Common base class: Employee
# Derived classes: Manager, Developer, Intern

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")

    def calculate_annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def manage_project(self):
        print(f"{self.name} is managing the {self.department} department.")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")

class Intern(Employee):
    def __init__(self, name, emp_id, salary, duration):
        super().__init__(name, emp_id, salary)
        self.duration = duration  # Internship duration in months

    def learn(self):
        print(f"{self.name} is learning during their {self.duration}-month internship.")

# Usage
print("----- Example 1: Employee Management System -----")
m = Manager("Hamna", "M101", 120000, "HR")
d = Developer("Ali", "D201", 90000, "Python")
i = Intern("Sara", "I301", 30000, 3)

m.show_info()
m.manage_project()

d.show_info()
d.write_code()

i.show_info()
i.learn()
print(f"Intern Annual Salary: {i.calculate_annual_salary()}")


# ------------------------------------------------
# 2️⃣ Example: Banking System
# ------------------------------------------------
# Base class: Account
# Derived classes: SavingsAccount, CurrentAccount

class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: {interest}. New balance: {self.balance}")

class CurrentAccount(Account):
    def __init__(self, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit!")

# Usage
print("\n----- Example 2: Banking System -----")
savings = SavingsAccount("Hamna", 5000)
current = CurrentAccount("Ali", 2000)

savings.deposit(1000)
savings.apply_interest()

current.withdraw(2500)
current.withdraw(1500)


# ------------------------------------------------
# 3️⃣ Example: Vehicle System
# ------------------------------------------------
# Base class: Vehicle
# Derived classes: Car, Bike, Truck

class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def show_details(self):
        print(f"Vehicle Brand: {self.brand}, Wheels: {self.wheels}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, 4)
        self.model = model
        self.fuel_type = fuel_type

    def show_details(self):
        print(f"Car: {self.brand} {self.model}, Fuel: {self.fuel_type}, Wheels: {self.wheels}")

class Bike(Vehicle):
    def __init__(self, brand, engine_capacity):
        super().__init__(brand, 2)
        self.engine_capacity = engine_capacity

    def show_details(self):
        print(f"Bike: {self.brand}, Engine Capacity: {self.engine_capacity}cc, Wheels: {self.wheels}")

class Truck(Vehicle):
    def __init__(self, brand, capacity_tons):
        super().__init__(brand, 6)
        self.capacity_tons = capacity_tons

    def show_details(self):
        print(f"Truck: {self.brand}, Capacity: {self.capacity_tons} tons, Wheels: {self.wheels}")

# Usage
print("\n----- Example 3: Vehicle System -----")
car = Car("Toyota", "Corolla", "Petrol")
bike = Bike("Honda", 150)
truck = Truck("Volvo", 20)

car.show_details()
bike.show_details()
truck.show_details()


# ------------------------------------------------
# 4️⃣ Example: Educational System
# ------------------------------------------------
# Base class: Person
# Derived classes: Student, Teacher, Administrator

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} (Student ID: {self.student_id}) is studying.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class Administrator(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def manage(self):
        print(f"{self.name} is managing {self.role} operations.")

# Usage
print("\n----- Example 4: Educational System -----")
student = Student("Zara", 20, "S123")
teacher = Teacher("Ahmed", 35, "Computer Science")
admin = Administrator("Sara", 40, "Admissions")

student.show_info()
student.study()

teacher.show_info()
teacher.teach()

admin.show_info()
admin.manage()


# ------------------------------------------------
# 5️⃣ Key Takeaways
# ------------------------------------------------
# ✅ Inheritance helps in building modular and scalable systems.
# ✅ It reduces code duplication by reusing common functionality.
# ✅ Child classes can extend or override parent behavior.
# ✅ It models real-world relationships effectively.


# ================================================
# Summary:
# - Inheritance allows child classes to reuse and extend parent features.
# - Real-world examples: Employee, Banking, Vehicle, and Education systems.
# - Promotes cleaner, organized, and reusable code structure.
# ================================================
