class employe:
    
    def calculate_salary(self):
        pass
        
class intern(employe):
    
    def calculate_salary(self,salary):
        salary=salary+salary*0.20
        print("Intern Salary: ",salary)
    
class FullTimeEmployee(employe):
    
    def calculate_salary(self,salary):
        salary=salary+salary*0.50
        print("Intern Salary: ",salary)
 
class ContractEmployee(employe):
    
    def calculate_salary(self,salary):
        salary=salary+salary*0.75
        print("Intern Salary: ",salary)
        
        
d1=ContractEmployee()
d2=FullTimeEmployee()
d3=intern()


d1.calculate_salary(5000)
d2.calculate_salary(10000)
d3.calculate_salary(110000)