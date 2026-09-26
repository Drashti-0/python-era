a = input("enter you string:")

char_freq={}

for char in a:
    if char not in char_freq:
        char_freq[char]=1
    else:
        char_freq[char]+=1
        
print(char_freq)