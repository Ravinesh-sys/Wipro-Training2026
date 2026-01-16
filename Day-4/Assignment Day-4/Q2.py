class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)



account1 = BankAccount(1001, 5000)
account2 = BankAccount(1002, 12000)


account1.display_details()
print()
account2.display_details()

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)



account = BankAccount(101, 5000)


account.display_details()
account.deposit(2000)
account.withdraw(3000)
account.display_details()

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("BankAccount object created")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def _del_(self):
        print("BankAccount object deleted for account:", self.account_number)



account = BankAccount(101, 5000)

account.display_details()
account.deposit(2000)
account.withdraw(1000)


del account




class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        # Proper validation checks
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
        elif amount > self.balance:
            print("Insufficient balance. Available balance:", self.balance)
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def _del_(self):
        print("BankAccount object deleted for account:", self.account_number)



account = BankAccount(101, 5000)

account.display_details()
account.deposit(2000)


account.withdraw(-500)
account.withdraw(10000)

# Valid withdrawal
account.withdraw(3000)

account.display_details()

del account