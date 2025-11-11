# ================================================
# File: Bank_Account_System.py
# Topic: OOP Project – Bank Account Management System
# ================================================

"""
This program demonstrates a simple **Bank Account System**
using Object-Oriented Programming (OOP) concepts in Python.

Concepts Used:
- Class and Objects
- Instance Variables and Methods
- Encapsulation (Private Members)
- Input Validation and Error Handling
- Basic Banking Operations (Deposit, Withdraw, Balance Inquiry)
"""

# ------------------------------------------------
# 1️⃣ Class Definition
# ------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Public attribute
        self.account_holder = account_holder
        
        # Private attribute (Encapsulation)
        self.__balance = balance

    # ------------------------------------------------
    # 2️⃣ Method to deposit money
    # ------------------------------------------------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ {amount} deposited successfully.")
        else:
            print("❌ Deposit amount must be greater than 0.")

    # ------------------------------------------------
    # 3️⃣ Method to withdraw money
    # ------------------------------------------------
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("❌ Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"✅ {amount} withdrawn successfully.")

    # ------------------------------------------------
    # 4️⃣ Method to check current balance
    # ------------------------------------------------
    def check_balance(self):
        print(f"💰 Current Balance: {self.__balance}")

    # ------------------------------------------------
    # 5️⃣ Getter Method (Access private balance)
    # ------------------------------------------------
    def get_balance(self):
        return self.__balance

    # ------------------------------------------------
    # 6️⃣ String Representation of the Account
    # ------------------------------------------------
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.__balance}"


# ------------------------------------------------
# 7️⃣ Usage Example
# ------------------------------------------------

def main():
    print("=== Welcome to the Bank Account System ===")

    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\nSelect an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Info")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print(account)

        elif choice == "5":
            print("Thank you for using the Bank Account System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


# ------------------------------------------------
# 8️⃣ Run the Program
# ------------------------------------------------
if __name__ == "__main__":
    main()
