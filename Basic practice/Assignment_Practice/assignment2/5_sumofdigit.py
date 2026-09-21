n=int(input("Enter number: "))


def fun(n):
    sum=0
    while(n!=0):
          reminder=n%10
          sum=sum+reminder
          n=n//10
    print(sum)
        
fun(n)
        
    