a=int(input("Enter number 1: "))
b=int(input("Ente rnumber 2: "))
operation=input("which sign you enter for operation? ")


def calculator(a,b,operation):
    if(operation=="addition"):
        c=a+b
        print("Addition: ",c)
        
    
    
    elif(opration=="substraction"):
        c=a-b
        print("substraction: ",c)
    
    
    elif(opration=="multiplication"):
            c=a*b
            print("Multiplication: ",c)
        
     
    elif(opration=="Divide"):
             c=a/b
             print("Divide: ",c)
         
    
calculator(a,b,operation)