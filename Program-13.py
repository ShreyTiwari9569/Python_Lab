class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        print("Savings Account Deposit")
        super().deposit(amount)

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print("Interest:", interest)

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self._BankAccount__balance = new_balance
            print("Current Account Withdrawal:", amount)
        else:
            print("Overdraft limit exceeded")


def show_account(account):
    account.display()
    print()

savings = SavingsAccount("Rahul", 10000, 5)
current = CurrentAccount("Aman", 5000, 2000)

print("   Savings Account ")
savings.deposit(2000)
savings.withdraw(1000)
savings.calculate_interest()
show_account(savings)

print("   Current Account ")
current.deposit(1000)
current.withdraw(2500)
show_account(current)