t=int(input())
for i in range(t):
    s=0
    p=[]
    a=input().replace(" ","")
    b=input().replace(" ","")
    c=sorted(a)
    d=sorted(b)
    f1=len(c)
    f2=len(d)
    if(c==d):
        print(0)
    else:
        if(f1<=f2):
            for j in range(f1):
                if c[j] in d:
                    p.append(c[j])
        else:
            for j in range(f2):
                if d[j] in c:
                    p.append(d[j])
        kj=len(c)-len(p)
        ks=len(d)-len(p)
        print(kj+ks)
        
    
