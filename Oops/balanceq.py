class BankAccount:
    
    def __init__(self):
        self.balance=0.0
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            return f"{self.balance:.2f} is the balance amount. Deposited is {amount}"
        else:
            return "Invalid deposit"
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance=self.balance-amount
                return f"{self.balance:.2f} is the balance amount. Withdrawn is {amount}"
            else:
                return "Insufficient funds"
        else:
            return "invalid deposit"
    def get_balance(self):
        return f"balance is {self.balance:.2f}"
        
obj1=BankAccount()
print(obj1.deposit(2500))
print(obj1.withdraw(1000))
print(obj1.get_balance())

