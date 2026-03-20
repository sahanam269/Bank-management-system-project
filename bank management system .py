
class BankAccount:
    def __init__(self, name, account_number, pin):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print("Current Balance:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter name: ")
        account_number = int(input("Enter account number: "))
        pin = input("Set PIN: ")

        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = BankAccount(name, account_number, pin)
            print("Account created successfully!")

    def login(self):
        account_number =int( input("Enter account number: "))
        pin = input("Enter PIN: ")

        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.pin == pin:
                print("Login successful!")
                self.account_menu(account)
            else:
                print("Wrong PIN!")
        else:
            print("Account not found!")

    def account_menu(self, account):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                amount = float(input("Enter amount: "))
                account.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter amount: "))
                account.withdraw(amount)

            elif choice == "3":
                account.check_balance()

            elif choice == "4":
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice!")


# Main Program
bank = Bank()

while True:
    print("\n1. Create Account\n2. Login\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.login()

    elif choice == "3":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice!")
