# Bank Account Management System

This project is a simple bank account management system implemented in Python. It allows you to create and manage different types of accounts, such as checking accounts and credit cards, and perform various transactions.


## Classes

- `BankAccounts`: This class represents a generic bank account (found in `banking.py`).
- `CreditCard`: This class represents a credit card (found in `creditcard.py`).
- `Separator`: This class is simply used for organization purposes within the terminal output. 

## Features

- Create and manage checking/savings accounts and credit cards
- Deposit and withdraw funds
- Transfer funds between accounts
- Create Debit & Credit Transactions for `BankAccounts`
- Create Credit Card transactions for `CreditCard`
- Pay off credit card balances by completing transfers between `BankAccounts` and `CreditCard`
- `BankAccounts` has overdraft charges put in place for accounts that go below $0.00
- `CreditCard` has Credit Limit that can be set. Transactions will not go through if amount forces the balance to exceed the Credit Limit

## Usage

Located in `application.py` is the executable code demonstrating how the classes integrate with one another. This can be modified to further test the classes and their abilities.

