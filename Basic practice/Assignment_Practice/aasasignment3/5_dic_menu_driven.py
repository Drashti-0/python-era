student = {
    "Drashti":98,
    "Dhruti":99,
    "Ayush":94,
    "Mantr":89,
    "yash":87
}


print("a.Add student")
print("b.Update marks")
print("c.search for student")
print("d.Display all student marks")

print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
enter=input("Enter your choice: ")

if enter == "a":
    student["mahil"]=95
    print(student)
    
elif enter== "b":
    student.update({"Mantr":91})
    print(student)
    
elif enter == "c":
    
    sname=input("Enter your student name: ")
    if sname in student:
        print("Marks:", student[sname])
    else:
        print("Student not found")
        
elif enter == "d":
        print(student)

else:
    print("Invalid choice")
