a=[1,2,2,2,3,4,4,5]
s=set()

for i in a:
    if a.count(i)>1:
        s.add(i)
        
print(s)
