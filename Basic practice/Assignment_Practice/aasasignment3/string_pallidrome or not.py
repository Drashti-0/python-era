a=input("Enter your string: ")

print(a)
#reverse the string
print(a[::-1])

if(a==a[::-1]):
    print("String is pallidrome")
    
else:
    print("String is not pallidrome")
    