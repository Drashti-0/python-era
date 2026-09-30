class bankacc:
    def __init__(self, acc_num, owner_name, bal):
        self.acc_num = acc_num
        self.owner_name = owner_name
        self.bal = bal

    def deposit(self):
        money = int(input("enter deposit money: "))
        #uperna koi variable ne use krvu hoy to ene apyu
        self.bal = self.bal + money
        print("total money", self.bal)
        print("Deposit successfully")
        
    def withdraw(self):
        print("withdraw successfully")
        
    def check_balance(self):
        print("balance check")    
         
        
d1 = bankacc(123456, "Drashti", 100000)

d1.deposit()
d1.withdraw()
d1.check_balance()