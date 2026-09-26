list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7, 8]

set1=set(list1)
set2=set(list2)

commun=set1.intersection(set2)

if(commun==set()):
    print("no commun")
    
else:
    print("commun")