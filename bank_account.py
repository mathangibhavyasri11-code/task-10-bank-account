# Q2. Define a class and constructor.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Encapsulation (private variable)
# Q3. Create attributes and methods.
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully.")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")
    def display_balance(self):
        print(f"Current Balance: {self.__balance}")
# Q4. Implement encapsulation.
# Encapsulation is done using private variable __balance.
# Q5. Use inheritance.
class SavingsAccount(BankAccount):
    pass
# Q6. Override methods.
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 50000:
            print("Withdrawal limit exceeded!")
        else:
            super().withdraw(amount)
# Q7. Create multiple objects.
print("=== Bank Account Simulation ===")
acc1 = SavingsAccount("Bhavya", 10000)
acc2 = CurrentAccount("Rahul", 80000)
# Q8. Simulate real bank operations.
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.display_balance()
print("--------------------------")
acc2.withdraw(60000)
acc2.display_balance()