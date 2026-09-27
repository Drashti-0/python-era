class Student:
    collagename = "abc"

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa


stu1 = Student("rahul", 9)

print(stu1.name)
print(Student.collagename)
print(stu1.collagename)