class bankacc:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
        
account1=bankacc("Drashti",5000)
account2=bankacc("Dhruti",100000)
account3=bankacc("Ayush",200000)

print(account1.account_holder,account1.balance)
print(account2.account_holder,account2.balance)
print(account3.account_holder,account3.balance)     