s = "hello"
ch = "l"
for i in range(len(s)): 
    if (s[i] == ch): 
        s = s[0 : i] + s[i + 1:] 
        break
for i in range(len(s) - 1,-1,-1):  
    if (s[i] == ch): 
        s = s[0 : i] + s[i + 1:] 
        break
print(s)