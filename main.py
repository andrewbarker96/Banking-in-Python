from Classes.BankAccounts import BankAccounts
from Classes.CreditCard import CreditCard

print()


def separator():
    print("-" * 50)
    


def main():
    # Accounts
    checkings = BankAccounts("CheckingAccount", "123 ABC Street", 7691, 1000, 2.50, 25)
    savings = BankAccounts("SavingsAccount", "123 ABC Street", 8007, 1000, 0, 50)
    creditcard1 = CreditCard("CreditCard", "123 ABC Street", 3352, 350, 3500, 21)

    # Starting Balances
    print(checkings)
    print(savings)
    print(creditcard1)

    separator()

    # Checkings Account Transactions
    checkings.debitTransaction(100)
    checkings.creditTransaction(5)
    checkings.withdraw(20)
    checkings.deposit(100)
    print(checkings)

    separator()

    # Transfering From Checkings into Savings
    checkings.transfer(savings, 250)
    print(checkings)
    print(savings)

    separator()

    # Transfering From Checkings into Credit Card
    checkings.transfer(creditcard1, 250)
    print(checkings)
    print(creditcard1)

    separator()

    # Checkings Account Overdraft Charge
    checkings.debitTransaction(473)
    print(checkings)

    separator()

    # Credit Card Limit Reached
    creditcard1.transaction(2999.99)
    print(creditcard1)

    separator()

    # Successful Credit Card Transaction
    creditcard1.transaction(225)
    print(creditcard1)

    separator()
    # Final Account Balances
    print(checkings)
    print(savings)
    print(creditcard1)


main()
print()
