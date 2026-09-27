class teacher:
    def __init__(self,salary):
        self.salary=salary

class student:
    def __int__(self,gpa):
        self.gpa=gpa
        
class ta(teacher,student):
    def __init__(self,salary,gpa,name):
        super().__init__(gpa)
        self.name=name
        
ta1=ta(15000,9.3,"Drashti")

print(ta1.name,ta1.salary,ta1.gpa)