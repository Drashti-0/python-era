class person:
    def __init__(self,name,age=0,address="Not given"):
        self.name=name
        self.age = age
        self.address = address
        
        
    def display(self):
        print("Name: ",self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        
p1=person("Drashti")
p2=person("Drashti",20)
p3=person("Drashti",20,"Anand")


p1.display()
p2.display()
p3.display()
    