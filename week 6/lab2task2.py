class Account:
    def  __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(F"${amount} deposited")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self , amount):
