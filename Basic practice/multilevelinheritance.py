class employee:
    start="10am"
    end="6pm"
    
    
class employee:
    start="10am"
    end="6pm"
    
class adminstaff(employee):
    def __init__(self,role):
        self.role=role
        
class accountant(adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary
        
acc1=accountant(250000,"CA")
print(acc1.salary,acc1.role,acc1.start,acc1.end )