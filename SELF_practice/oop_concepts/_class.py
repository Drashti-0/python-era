class student:
    name="Drashti"
    branch="CSE"
    semester=3
    
    def __init__(self,name,branch,semester):
        self.name=name
        self.branch=branch
        self.semester=semester
        
    def introduce(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Semester:", self.semester)
        
st1 = student("Drashti", "CSE", 3)
st1.introduce()
    
