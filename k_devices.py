import math

n,k=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
l=[]
for i in range(n):
    s=x[i]**2+y[i]**2
    s=s**0.5
    l.append(math.ceil(s))
l.sort()
print(l[k-1])
