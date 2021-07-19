import math
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in range(n):
        l[i]=math.ceil(l[i]/m)
    c=n-l[::-1].index(max(l))
    print(c)
