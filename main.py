from classes import BankAccount

# Instantiate several instances of the BankAccount class
accounts = [
    BankAccount("Jane Doe", 500.00, "345348293"),
    BankAccount("John Doe", 200.00, "234238254"),
    BankAccount("Frank Lee", 900.00, "3453443463")
]

def prompt_user_for_action(account):
    """A function to prompt the user for desired account actions"""
    print(account.display_account_info())
    action = input("Would you like to deposit (d) or withdraw (w) money? ").lower()

    if action == 'd':
        d_prompt = input("Enter the amount you would like to deposit: ")
        amount = float(d_prompt.replace('$', '').replace(',', '').strip())
        result = account.deposit(amount)
        if isinstance(result, float):
            print(f"Deposit successful. New balance: ${result:,.2f}.")
        else:
            print(result)
    elif action == 'w':
        w_prompt = input("Enter the amount you wish to withdraw: ")
        amount = float(w_prompt.replace('$', '').replace(',', '').strip())
        print(account.withdraw(amount))
    else:
        print("Invalid action. Please enter 'd' to deposit or 'w' to withdraw.")
        print(account.withdraw(amount))

# Call the display_account_info() method on each of the accounts
for index, account in enumerate(accounts):
    print(account.display_account_info())
