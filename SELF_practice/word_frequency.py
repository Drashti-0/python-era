a=input("Enter your string: ")

words=a.split()

frequency={}

for word in words:
    if word not in frequency:
        frequency[word]=1
        
    else:
        frequency[word]+=1
print(frequency)