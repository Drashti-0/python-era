n=int(input("Enter number: "))

def function(n):
    count=0
    while(n!=0):
        reminder=n%10
        count+=1
        n=n//10
   
    print("Total digits are: ",count)
    
function(n)