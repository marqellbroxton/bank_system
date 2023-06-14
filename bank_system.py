
class Account:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.balance = 0.0
        self.mainMenu()

    def mainMenu(self):
        print("\nWelcome to Broad Bank\n")
        while True:
            print("1. View Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Please select an option: ")

            if choice == "1":
                self.viewBalance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using Broad Bank. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def viewBalance(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Balance: ${self.balance:.2f}")
        print()


    def deposit(self):
        amount = float(input("\nEnter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited into your account.")
            self.viewBalance()
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self):
        amount = float(input("\nEnter the amount to withdraw: "))
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount:.2f} has been withdrawn from your account.")
                self.viewBalance()
            else:
                print("Insufficient funds. Withdrawal failed.")
        else:
            print("Invalid amount. Withdrawal failed.")

Account()