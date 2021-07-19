import numpy as np
t=int(input())
for _ in range(t):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    sub=np.array_split(a,k)
    p=[]
    for i in sub:
        p.append(min(i))
    if(min(p)<q):
        print(min(p))
    else:
        print("NO")
