"""A file to hold the parent class and all child classes"""

class BankAccount():
    """This class provides a structure to model a bank account and common actions related to banking, such as deposits and withdrawals."""
    def __init__(self, account_holder: str, __account_balance: float, account_number: str) -> None:
        self.account_holder = account_holder # attribute to hold name of account holder
        self.__account_balance = __account_balance # attribute to hold account balance
        self.account_number = account_number # attribute to hold account number

    def greeting(self):
        return f"Hello, {self.account_holder}!"

    def deposit(self, amount: float):
        """Class method to enable user to make a deposit to their account"""
        if amount > 0:
            self.__account_balance += amount
            return self.__account_balance
        else:
            return "It is not possible to deposit a negative amount. "\
                "Please enter a positive number."

    def withdraw(self, amount: float):
        """Class method to enable user to make a withdrawal from their account"""
        if self.__account_balance < amount:
            return f"Insufficient funds. You cannot withdraw more than your current balance of ${self.__account_balance:,.2f}. Please try again."
        else:
            self.__account_balance -= amount
            return f"{self.greeting()} Your withdrawal was successful. {self.get_balance()}"

    def get_balance(self):
        """Class method to enable user to access the current balance of their account"""
        return f"Your current balance for account number {self.account_number} is ${self.__account_balance:,.2f}."

    def display_account_info(self):
        """Class method to enable user to display all attributes of their account"""
        return f"Hello, {self.account_holder}! {self.get_balance()}"
