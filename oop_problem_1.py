class BankAccount:
    """Problem 1: Bank Accounts
    Create a BankAccount class with attributes account_number, account_holder, and balance.
    Include methods for depositing, withdrawing, and checking the balance.
    Implement a SavingsAccount class that inherits from BankAccount, with an additional attribute interest_rate.
    Override the deposit() method to add an interest based on the interest rate whenever money is deposited."""

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Your balance {self.balance} now"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount}. Your actual balance {self.balance}"
        else:
            return "Insufficient balance"

    def check_balance(self):
        return f"Your actual balance {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, percent):
        super().__init__(account_number, account_holder, balance)
        self.percent = percent

    def deposit(self, amount):
        self.balance += amount
        earned_percent = amount * (self.percent / 100)
        self.balance += earned_percent
        return f"Deposited {amount}. Your actual balance {self.balance}"


account1 = BankAccount("12345", "Mr.Smith", 1000)
account1.deposit(500)
account1.withdraw(200)
print(account1.check_balance())

savings_account = SavingsAccount("54321", "Ms.Smith", 2000, 2.5)
savings_account.deposit(1000)
print(savings_account.check_balance())
