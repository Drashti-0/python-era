class leptop:
    stg="ssd"
    
    def __init__(self,ram,storage):
        self.ram=ram
        self,storage=storage
        
        @classmethod
        def get_stg(cls):#class Attributes
            print(f"Storage = {cls.stg}")
          
         def get_info(self):#instance variable
             print(f"laptop has {self.ram}ram &{self.storage} {self.storage}")   

l1=leptop("16gb0""512gb) 
          
fnx=>(price,discount)=>final price