class shape:
    def area(self):
        pass
        
        
class circle(shape):
    def area(self):
        print("cicle is called!")
    
    
    
class rectangle(shape):
    def area(self):
        print("rectangle is called!")
        
    

class triangle(shape):
    def area(self):
        print("triangle is called!")
        
d1=triangle()
d2=rectangle()
d3=triangle()


d1.area()
d2.area()
d3.area()