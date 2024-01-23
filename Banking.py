import separator
from creditcard import CreditCard


class BankAccounts:
    def __init__(
        self, name, address, accountNumber, __balance, __creditFee, overdraftFee
    ):
        self.name = name
        self.address = address
        self.accountNumber = accountNumber
        self.__balance = float(__balance)
        self.__creditFee = __creditFee
        self.overdraftFee = overdraftFee

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        while self.__balance - amount >= 0:
            self.__balance -= amount
            break
        else:
            print("Insufficient funds")
            return None

    def debitTransaction(self, amount):
        self.__balance -= amount

    def creditTransaction(self, amount):
        self.__balance -= amount
        self.__balance -= self.__creditFee

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        if isinstance(target_account, BankAccounts):
            target_account.deposit(amount)
        elif isinstance(target_account, CreditCard):
            target_account.deposit(amount)
        print(
            f"Transfer of ${amount:,.2f} from {self.name}-{self.accountNumber} to {target_account.name}-{target_account.accountNumber}"
        )
    
    def __str__(self):
        if self.__balance >= 0:
            return f"{self.name}-{self.accountNumber} Balance = ${self.__balance:,.2f}"
        else:
            balance_with_fee = self.__balance - self.overdraftFee
            return f"Account Balance Negative\nOverdraft Fee ${self.overdraftFee:,.2f} Applied\n{self.name}-{self.accountNumber} Balance = ${balance_with_fee:,.2f}"
