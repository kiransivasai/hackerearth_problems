import numpy as np
t=int(input())
for _ in range(t):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    p=min(a)
    j=max(a)
    if(k==1):
        if(j<=q):
            print(j)
        else:
            print("NO")
    else:
        if(p<=q):
            print(p)
        else:
            print("NO")
