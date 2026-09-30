class student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
        
        
    def getter(self):
        print("Name: ",self.__name)
        print("Roll no. : ",self.__roll_no)
        print("Marks: ",self.__marks)
        
        
    def setter(self,name,roll_no,marks):
        if name=="" :
            print("number is empty")
        elif roll_no < 1 or roll_no > 100:
            print("Roll number must be between 1 and 100")
        elif marks < 0:
            print("Marks cannot be negative")  
        else:
            self.__name = name
            self.__roll_no = roll_no
            self.__marks = marks
            
            
s1 = student("Drashti", 10, 85)

s1.getter()

s1.setter("Drashti", 20, 90)

s1.getter()