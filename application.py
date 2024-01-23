from Banking import Bank
from Banking import CreditCard
from separator import Separator

print()


def main():
    # Accounts
    account1 = Bank("CheckingAccount", "123 ABC Street", 7691, 1000, 2.50, 25)
    account2 = Bank("SavingsAccount", "123 ABC Street", 8007, 1000, 0, 50)
    creditcard1 = CreditCard("CreditCard", "123 ABC Street", 3352, 350, 3500, 21)

    # Starting Balances
    print(account1)
    print(account2)
    print(creditcard1)

    Separator()

    # Transfering From Checkings into Savings
    account1.transfer(account2, 250)
    print(account1)
    print(account2)

    Separator()

    # Transfering From Checkings into Credit Card
    account1.transfer(creditcard1, 250)
    print(account1)
    print(creditcard1)


main()
print()
