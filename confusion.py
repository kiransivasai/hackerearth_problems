from collections import Counter
n,q=map(int,input().split())
a=list(map(int,input().split()))
c=len(Counter(a))
if(c==n):
    for i in range(q):
        b=int(input())
        print(len(a[b-1:]))
elif(c==1):
    for i in range(q):
        b=int(input())
        print(1)
else:
    for i in range(q):
        b=int(input())
        d=len(Counter(a[b-1:]))
        print(d)
    
    
