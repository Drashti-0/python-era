class dog:
             
    def __init__(self,name,age):
        self.name=name
        self.age=age
 
    def bark(self):
        print(self.name, "is barking!")
        
dog1 = dog("Tommmy",3)           
    
dog1.bark()