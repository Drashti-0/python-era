'''Write a function that returns if is a prime number and
otherwise, using a loop'''

n=int(input("Enter a number: "))

a=int(input("Enter ending Range"))

def funcation(n,a):
    for n in range(2,a):
        if n>1: 
            