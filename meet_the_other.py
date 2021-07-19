for _ in range(int(input())):
    n=int(input())
    s=[]
    ind=[]
    m=10000
    for i in range(n):
        a=input()
        s.append(a)
        ind.append(i)
    s,ind=zip(*sorted(zip(s,ind)))
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            d=ind[i+1]-ind[i]
            if(d<m):
                m=d
    if(m==10000):
        print(-1)
    else:
        print(m)
