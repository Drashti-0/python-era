class employee:
    strt="10 am"
    end="6 pm"
    
class teacher(employee):
    def __init__(self,subject):
        self.subject=subject
        
class admin(employee):
    def __init__(self,role):
        self.role = role
        
a1=admin("manager")
t1=teacher("MATHS")

print(a1.role,a1.strt,a1.end)
print(t1.subject,t1.strt,t1.end)