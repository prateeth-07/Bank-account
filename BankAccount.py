class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
            else:
                print("Insufficient funds. Withdrawal failed.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")


class Menu:
   
    def show_menu():
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Current Balance")
        print("4. Exit")



def main():
    account_holder_name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))

    account = BankAccount(account_holder_name, account_number, initial_balance)

    while True:
        Menu.show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Thank you. Bye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
