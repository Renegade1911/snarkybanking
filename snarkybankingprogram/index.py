class Account:
    def __init__(self, username, password, amount):
        self.username = username
        self.password = password
        self.amount = amount

    def __repr__(self):
        return f"Account({self.username},{self.amount})"


class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self, username, password, amount):
        for i in self.accounts:
            if i.username == username:
                return "Username already exists. Please be original for once."

        new = Account(username, password, amount)
        self.accounts.append(new)
        return "Account created successfully. Now let's make irresponsible decisions!"

    def get_account(self, username, password):
        for i in self.accounts:
            if i.username == username and i.password == password:
                return i
            return False

    def withdraw(self, username, password, amount):
        account = self.get_account(username, password)
        if account == False:
            return "Invalid Username/Password. Don't try so hard, idiot."

        if amount > account.amount:
            return "Insufficient Balance. Don't kid yourself lmao."

        if amount > 0:
            account.amount -= amount
            return "Withdraw Successful. Don't spend it all in one place."
        else:
            return "Invalid amount. Lookin' dry here, bud."

    def deposit(self, username, password, amount, account=None):
        account = self.get_account(username, password)
        if account == False:
            return "Invalid Username/Password. Don't try so hard, idiot."
        if amount > 0:
            account.amount += amount
            return "Deposit Successful. Don't worry, we'll keep it safe... Promise."
        else:
            return "Invalid Amount lmao."


BANK = BankSystem()

output = BANK.create_account(username='coder', password='123', amount=2000)

print(output)
output = BANK.deposit(username='coder', password='123', amount=1000)

print(output)
output = BANK.withdraw(username='coder', password='123', amount=1000)

print(output)
