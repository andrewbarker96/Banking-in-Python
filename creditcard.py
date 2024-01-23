class CreditCard:
    def __init__(self, name, address, accountNumber, __balance, limit, interest):
        self.name = name
        self.address = address
        self.accountNumber = accountNumber
        self.__balance = float(__balance)
        self.limit = float(limit)
        self.interest = float(interest * 0.01)

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance -= amount

    def transaction(self, amount):
        if self.__balance + amount <= self.limit:
            self.__balance += amount
            return self.__balance
        else:
            print("Transaction Declined")

    def __str__(self):
        return f"{self.name}-{self.accountNumber} Balance = ${self.__balance:,.2f}"
