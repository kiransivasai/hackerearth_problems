s=input()
if(s[::-1]==s):
    a=s[0]
    b=s[:(len(s)//2)]
    c=0
    for i in b:
        if(i!=a):
            break
        else:
            c+=1
    if(c==len(s)//2):
        print(0)
    else:
        print(len(s)-1)
else:
    print(len(s))
