 
n,k,x=map(int,input().split())
a=[i for i in range(1,n+1)]

w=0
while(len(a)>1):
    c=x%k
    p=a.index(x)+1
    for i in range(c):
        p%=len(a)
        a.pop(p)
        if(len(a)==1):
            w=a[0]
            break
        p%=len(a)
    if(w>0):
        break
    x=a[p]
if(w>0):
    print(w)
else:
    print(a[0])
