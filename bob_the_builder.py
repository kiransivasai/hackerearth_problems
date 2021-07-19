from collections import Counter
n=int(input())
a=list(map(int,input().split()))
c=Counter(a)
b=0
for i in c:
    m=c[i]
    if(m>b):
        b=m
d=[]
for i in c:
    if(c[i]==b):
        d.append(i)
print(min(d))
