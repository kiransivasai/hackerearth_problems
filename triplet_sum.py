from itertools import permutations as per
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
p=[]
l=per(a,3)
for i in l:
    k=sum(i)
    if(k%m==0):
        p.append(k)
        if(len(p)==20):
            break
if(len(p)!=0):
    print(max(p))
else:
    print(-1)
