
accounts = {} 

class BankSystem:
    def create_new_acct(self, account_name, account_balance=0.0):
        if account_name not in accounts:
            accounts[account_name] = Account(account_name, account_balance)
            print("Account successfully created!")
        else:
            print("Account already exists.")
        
    def delete_account(self, account_name):
        if account_name in accounts:
            del accounts[account_name]
            print("Account deleted successfully!")
        else:
            print("Account does not exist!")    
        
class Account:
    def __init__(self, account_name, account_balance):
        self.account_name = account_name
        self.account_balance = account_balance
        
    def get_acct_details(self):
        print(f"Account Details:\nAccount Name: {self.account_name}\nBalance: ${self.account_balance}")
        
    def deposit_money(self):
        try:
            deposit = int(input("How much do you want to deposit? "))
            self.account_balance += deposit
            print(f"Deposit successful! Your current balance is ${self.account_balance}")
        except ValueError:
            print("enter an integer.")    
        
    def withdraw(self):
        try:
            withdrawal = int(input("How much do you want to withdraw? "))
            if withdrawal > self.account_balance:
                print(f"Insufficient funds. You have ${self.account_balance}.")
            else:
                self.account_balance -= withdrawal
                print(f"Withdrawal successful! Your current balance is ${self.account_balance}")
        except ValueError:
            print("enter an integer.")   
     
    def check_balance(self):
        print(f"Current Balance: ${self.account_balance}")

bank = BankSystem()

print("""Welcome to this simple banking system:
         1 - Create an account
         2 - Make a deposit
         3 - Make a withdrawal
         4 - Get account info
         5 - Check balance
         6 - Delete an account
         7 - exit""")
            
while True:
    try:
        user_input = int(input("What would you like to do? "))
        if user_input == 1:
            account_name = input("Enter account name: ")
            bank.create_new_acct(account_name)
        elif user_input == 2:
            account_name = input("Enter account name: ")
            if account_name in accounts:
                accounts[account_name].deposit_money()
            else:
                print("Account not found.")
        elif user_input == 3:
            account_name = input("Enter account name: ")
            if account_name in accounts:
                accounts[account_name].withdraw()
            else:
                print("Account not found.")
        elif user_input == 4:
            account_name = input("Enter account name: ")
            if account_name in accounts:
                accounts[account_name].get_acct_details()
            else:
                print("Account not found.")
        elif user_input == 5:
            account_name = input("Enter account name: ")
            if account_name in accounts:
                accounts[account_name].check_balance()
            else:
                print("Account not found.")
        elif user_input == 6:
            account_name = input("enter account name: ")
            if account_name in accounts:
                del accounts[account_name]
                print("Account successfully deleted")
            else:
                print("Account not found.")            
        elif user_input == 7:
            print("Thank you for using my banking system!")
            break
        else:
            print("Please enter a valid option.")
    except ValueError:
        print("Enter a number.")
