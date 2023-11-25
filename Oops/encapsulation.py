class BackAccount:
    def __init__(self,account_number,account_holding):
        self.account_number=account_number
        self.account_holding=account_holding
        self._balance=0.0 #protected member
    def deposit(self,amount):
        self._balance=self._balance+amount
        return f"account number {self.account_number} and account holder {self.account_holding} : the balance is {self._balance:.2f} and the deposited amount is {amount}"
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance=self._balance-amount
            return f"account number {self.account_number} and account holder {self.account_holding} : the balance is {self._balance:.2f} and the withdrawn amount is {amount}"
    def get_balance(self):
        return f"the current balance is {self._balance:.2f}"

obj1=BackAccount(12345,'Deepak Sharma')

print(obj1.deposit(12000))
print(obj1.withdraw(2000))
print(obj1.deposit(13000))
print(obj1.get_balance())



             
             