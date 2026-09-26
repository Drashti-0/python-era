set={1,2,2,3,4,4,4,5}

once=print(set)
count=0

for i in set:
    if i in set:
        count=count+1

print(count)
