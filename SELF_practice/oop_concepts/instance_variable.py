class rectanngle:
    #counstructor  
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    #method    
    def area(self):
            return self.length*self.width
        
    def perimeter(self):
        return 2*(self.length+self.width)
  
    
r1=rectanngle(10,5)
print("Area: ",r1.area())
print("Perimeter: ",r1.perimeter())
