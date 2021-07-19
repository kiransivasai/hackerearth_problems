import collections
n=int(input())
l=[]
for _ in range(n):
    l.append(input())
l.sort()
c=collections.Counter(l)
a=list(c.keys())
b=list(c.values())
for i in range(len(b)):
    for j in range(len(b)-i-1):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
a=a[::-1]
b=b[::-1]
i=0
print(len(a))
while(i!=len(a)):
    x=len(b)-b[::-1].index(b[i])
    y=b.index(b[i])
    if(x-y==1):
        print(a[i])
        i+=1
    else:
        k=a[y:x]
        k.sort()
        for j in k:
            print(j)
        i+=len(k)
