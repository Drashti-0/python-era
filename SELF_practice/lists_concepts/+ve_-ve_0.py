numbers = [10, -5, 0, 8, -2, 0, 15, -7]

for i in numbers:
    count =0
    xx=0
    xxx=0
    if(i>0):
        count=count+1
        
    elif(i<0):
       xx=xx+1
       
    else:
       xxx=xxx+1
        
print("POSITIVE COUNT IS:",count)

print("NEGAATIVE COUNT IS: ",xx)

print("ZERO COUNT IS: ",xxx)