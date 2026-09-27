class employee:
    def get_desigation(self):
        print("Empoyee")
        
class teacher(employee):
    def get_desigation(self):
        print("Teacher")
        
t1=teacher()
t1.get_desigation()
    