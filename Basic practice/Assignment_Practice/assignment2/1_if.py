salary=int(input("Enter your salary: "))

if salary<30000:
    tax = 0.05
    slary = salary +(salary* tax)
    print("Total amt: ",salary)

elif salary>=30000 and salary<70000:
    tax=0.15
    salary=salary + (salary*0.15)
    print("Total amt: ",salary)
    
else:
    tax=0.25
    salary=salary + (salary*0.25)
    print("total amt: ",salary)