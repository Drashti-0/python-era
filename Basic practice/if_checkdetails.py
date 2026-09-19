''' username = input("Enter your valied username: ")
password = input("Enter your valied password: ")

if username=="Admin" and password=="Admin123":
    print("You are successfully login in")
    
elif username!="Admin":
    print("Invalied Username")
    
elif password!="Admin123":
    print("Invalied Password")
    
else:
    print("Your detils is incorrected") '''
    
    
    #using nested if else
    
    
username = input("Enter your valied username: ")
password = input("Enter your valied password: ")


if username=="Admin" and password=="Admin123":
    print("You are successfully login in")

else:
    if username != "Admin":
        print("Your username is incorrect")
    
    else:
        print("Password is incorrect")