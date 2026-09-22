
while True:
    
    n=int(input("enter number: "))
    a=57
    
    if n==a:
        print("You gusse correct word!")
        break
    
    if(n>a):
        print("Too High")
    elif(n<a):
        print("Too Low")

