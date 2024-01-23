class CreditCard:
    def __init__(self, name, address, accountNumber, __balance, credit_limit, interest):
        self.name = name
        self.address = address
        self.accountNumber = accountNumber
        self.__balance = float(__balance)
        self.credit_limit = float(credit_limit)
        self.interest = float(interest * 0.01)

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance -= amount

    def transaction(self, amount):
        if self.__balance + amount <= self.credit_limit:
            self.__balance += amount
        else:
            print(f"Transaction Declined - Charge ${amount} Exceeds Account's Available Credit credit_Limit of ${self.credit_limit:,.2f}")

    def __str__(self):
        return f"{self.name}-{self.accountNumber} Balance = ${self.__balance:,.2f}"
