for _ in range(int(input())):
    n=input()
    m=0    
    a="0123456789"
    q=""
    d={}
    for i in n:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in a:
        if i in d:
            if d[i]>m:
                m=d[i]
                q=i
    print(q)
