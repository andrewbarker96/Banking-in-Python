# Bank Account Management System

This project is a simple bank account management system implemented in Python. It allows you to create and manage different types of accounts, such as checking accounts and credit cards, and perform various transactions.

## Classes

- `BankAccount`: This class represents a generic bank account (found in the folder `Classes` labeled `BankAccount.py`).
- `CreditCard`: This class represents a credit card (found in folder `Classes` labeled `CreditCard.py`).

## Features

- Create and manage checking/savings accounts and credit cards
- Deposit and withdraw funds
- Transfer funds between accounts
- Create Debit & Credit Transactions for `BankAccount`
- Create Credit Card transactions for `CreditCard`
- Pay off credit card balances by completing transfers between `BankAccount` and `CreditCard`
- `BankAccount` has overdraft charges put in place for accounts that go below $0.00
- `CreditCard` has Credit Limit that can be set. Transactions will not go through if amount forces the balance to exceed the Credit Limit

## Usage

Located in `main.py` is the executable code demonstrating how the classes integrate with one another. This can be modified to further test the classes and their abilities.
