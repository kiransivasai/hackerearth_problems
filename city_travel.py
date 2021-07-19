import math
s,x,n=map(int,input().split())
d={}
for _ in range(n):
    t,y=map(int,input().split())
    d[t]=y
dk=d.keys()
ld=len(dk)
pv=sum(d.values())
p=math.ceil((s-pv)/x)
c=ld+p
if(c>0 and p>0):
    print(c)
else:
    ts=0
    j=1
    while(ts<s):
        if j in dk:
            ts+=d[j]
        else:
            ts+=x
        j+=1
    print(j-1)
