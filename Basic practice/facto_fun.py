
def cal_facto(n):
    facto=1
    
    for i in range(1,n+1):
        facto *= i
        
    return facto
   
   
n=int(input("Enter number: "))   
print(cal_facto(n))