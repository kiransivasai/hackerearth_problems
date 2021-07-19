p=input()
s=""
for i in p:
    if(i.islower()):
        s=s+i.upper()
    elif(i.isupper()):
        s=s+i.lower()
    else:
        s=s+i
print(s)
