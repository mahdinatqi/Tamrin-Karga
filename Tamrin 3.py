class BankAcount:
    def init(self, blnc,intrst):
        self.balance = blnc
        self.interest_rate = intrst
        
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,amount):
        result = self.balance - amount
        return result
    
    def add_interest(self):
        interest = self.balance*(self.interest_rate/12)
        self.balance = self.balance + interest
        return
    
    def get_balance(self):
        return self.balance
    
        
B_c1 = BankAcount(2000,0.012)
n = 300
print(f"Your account is added {n} and is now {B_c1.deposit(n)}")
print(f"Your account is cut {n} and is now {B_c1.withdraw(n)}")