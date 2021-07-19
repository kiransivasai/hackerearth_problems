from collections import Counter
n=int(input())
a=list(map(int,input().split()))
e=0
c=list(dict(Counter(a)).keys())
d=list(dict(Counter(a)).values())
b=[]
for i in range(len(c)):
    if(d[i]==1):
        b.append(c[i])
        e+=1
    if(e==2):
        break

b.sort()
for i in b:
    print(i,end=" ")
