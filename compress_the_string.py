for _ in range(int(input())):
    n=int(input())
    s=list(input())
    c=s[0].upper()
    s.pop(0)
    v=['a','e','i','o','u']
    i=0
    d=0
    for i in range(len(s)):
        if(s[i] in v and s[i]!=c[-1]):
            if(d>0):
                c+=str(d)
                d=0
            c+=s[i]        
        elif(s[i] not in v):
            d+=1
        else:         
            if(d>0):
                c+=str(d)
                d=0
                c+=s[i]
    if(d>0):
        c+=str(d)
    print(c)
