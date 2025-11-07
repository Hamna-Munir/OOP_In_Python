# ===============================================================
# File: 03_Hiding_Implementation_Details.py
# Topic: Hiding Implementation Details using Abstraction
# ===============================================================

"""
In Object-Oriented Programming, **Abstraction** helps to hide the complex 
implementation details and show only the **essential functionalities** 
to the user.

This concept is often referred to as **Data Hiding** or **Encapsulation of Behavior**.

The user interacts with the system through **simple interfaces** (methods),
without knowing how things actually work internally.
"""


# ---------------------------------------------------------------
# 1️⃣ Why Hide Implementation Details?
# ---------------------------------------------------------------

"""
Hiding implementation details:
- Prevents misuse or accidental modification of internal logic.
- Simplifies usage for end-users.
- Makes the program easier to maintain and extend.
- Improves security by controlling what can be accessed externally.

For example:
When you call a `withdraw()` method in a banking application,
you are not concerned with how the bank updates its databases internally.
"""


# ---------------------------------------------------------------
# 2️⃣ Example: Bank Account (Without Hiding Implementation)
# ---------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")


# Usage (User directly accessing internal variable)
account1 = BankAccount("Hamna", 1000)
account1.deposit(500)
account1.withdraw(300)

# Problem: The user can directly modify balance (not secure)
account1.balance = -9999   # ❌ Dangerous: Breaks data integrity
print("Balance after unauthorized change:", account1.balance)


# ---------------------------------------------------------------
# 3️⃣ Solution: Hide Implementation using Abstraction
# ---------------------------------------------------------------

"""
We use:
- A single underscore `_variable` to indicate a **protected** member (internal use).
- A double underscore `__variable` to make a **private** member (name mangling).

We then provide **public methods** (getters/setters) to safely access or modify data.
"""

class SecureBankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner          # Private attribute
        self.__balance = balance      # Private attribute

    # Public interface (accessible by user)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Invalid or insufficient funds!")

    # Safe way to check balance
    def check_balance(self):
        print(f"Current balance: ${self.__balance}")


# Usage
print("\n--- Secure Bank Account Example ---")
secure_acc = SecureBankAccount("Ali", 2000)
secure_acc.deposit(1000)
secure_acc.withdraw(500)
secure_acc.check_balance()

# Trying to access private variable directly
# print(secure_acc.__balance)  # ❌ AttributeError: 'SecureBankAccount' object has no attribute '__balance'


# ---------------------------------------------------------------
# 4️⃣ Hiding Implementation in Complex Systems
# ---------------------------------------------------------------

"""
Abstraction is especially useful in large systems like:
- Databases (SQL operations hidden behind ORM)
- Web frameworks (Django hides HTTP handling)
- Machine Learning libraries (TensorFlow, PyTorch hide low-level math)

Developers only work with **simple interfaces** rather than the complex underlying logic.
"""

class EmailService:
    def send_email(self, recipient, subject, message):
        self.__connect_to_server()
        self.__authenticate()
        print(f"Sending email to {recipient} with subject '{subject}'...")
        self.__disconnect()
        print("Email sent successfully!")

    # Private methods (implementation details)
    def __connect_to_server(self):
        print("(Connecting to mail server...)")

    def __authenticate(self):
        print("(Authenticating user credentials...)")

    def __disconnect(self):
        print("(Disconnecting from mail server...)")


# Usage
print("\n--- Email Service Example ---")
email = EmailService()
email.send_email("user@example.com", "Meeting Reminder", "Don't forget the meeting at 3 PM.")

# User cannot call these directly:
# email.__connect_to_server()  # ❌ Raises AttributeError


# ---------------------------------------------------------------
# 5️⃣ Real-World Example: Car System
# ---------------------------------------------------------------

"""
When you start a car, you just press the start button.
You don’t see or control how:
- the fuel pump activates,
- spark plugs ignite,
- or how the engine cycles start internally.

Abstraction hides all those internal steps from the user.
"""

class Car:
    def start(self):
        self.__ignite_engine()
        self.__check_systems()
        print("Car started successfully!")

    # Hidden internal processes
    def __ignite_engine(self):
        print("(Igniting the engine...)")

    def __check_systems(self):
        print("(Checking all systems...)")


# Usage
print("\n--- Car System Example ---")
car = Car()
car.start()

# User cannot manually call internal processes
# car.__ignite_engine()  # ❌ Not accessible outside the class


# ---------------------------------------------------------------
# 6️⃣ Advantages of Hiding Implementation Details
# ---------------------------------------------------------------

"""
✅ Prevents accidental or unauthorized access to sensitive data.
✅ Makes the system easier to use (users see only what’s necessary).
✅ Simplifies maintenance by isolating internal logic.
✅ Improves data security and reduces bugs.
✅ Encourages modular, reusable, and maintainable code.
"""


# ---------------------------------------------------------------
# 7️⃣ Key Points
# ---------------------------------------------------------------

"""
- Abstraction focuses on **what to do**, not **how to do it**.
- Implementation details are hidden using:
    → Single underscore `_var` (protected)
    → Double underscore `__var` (private)
- Public methods (getters/setters) act as safe interfaces.
- It ensures a clear separation between user interaction and internal logic.
"""


# ===============================================================
# Summary:
# Hiding implementation details → Protects internal logic and exposes only 
# essential methods for user interaction.
# ===============================================================
