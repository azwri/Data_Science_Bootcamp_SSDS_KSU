import time

class Bank:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount=0):
        while True:
            amount = input("Enter the amount: ")
            try:
                amount = float(amount)
                if amount > 0:
                    self.balance += amount
                    print("Thank You, your transaction is done.\n")
                    print("#######################################")
                    time.sleep(3)
                    break
                else:
                    print("Error, you must deposit more than 0.")
                    time.sleep(3)
            except:
                print("Error, enter correct amount.")
                time.sleep(3)
    
    def withdraw(self):
        while True:
            amount = input("Enter the amount: ")
            try:
                amount = float(amount)
                if amount > 0:
                    self.balance -= amount
                    print("Thank You, your transaction is done.\n")
                    print("#######################################")
                    time.sleep(3)
                    break
                else:
                    print("Error, you must withdraw more than 0.")
                    time.sleep(2)
            except:
                print("Error, enter correct amount.")
                time.sleep(3)
    
    def get_balance(self):
        return self.balance
        
    
account = Bank()
while True:
    print(f"""Welcome to SSDS_KSU Bank \U0001F3E6

Please enter a number for the options:

    1-> Deposit Cash
    2-> Withdraw Cash
    3-> Check Balance
    4-> Exit
    
#######################################""")
    
    choise = input("Enter your option: ")
    if choise not in ['1', '2', '3', '0']:
        print("Error, choose 1, 2, 3 or 0 to exit.")

    elif choise == '1':
        account.deposit()
    elif choise == '2':
        account.withdraw()
    elif choise == '3':
        print(f"Your balance is : {account.get_balance()}")
        time.sleep(3)
    else:
        print("Thank you for useing SSDS_KSU Bank \U0001F3E6.")
        time.sleep(3)
        break