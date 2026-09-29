class leptop:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.prrice=price
        
lep1=leptop("dell","8gb",50000)
lep2=leptop("HP","16gb",100000)

print("leptop 1: ",lep1.brand,lep1.ram,lep1.price)
print("leptop 2: ",lep2.brand,lep2.ram,lep2.price)
