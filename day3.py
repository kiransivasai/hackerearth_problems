from itertools import combinations_with_replacement as cwr
from itertools import permutations as per
n,m,l=map(int,input().split())
li=list(map(int,input().split()))
alp=list(cwr(li,n))
perm=list(per(li,n))
print(perm)
print(alp)
ans=0
for i in alp:
    if(sum(i)%m==0):
        ans+=1
print(ans%(10**9+7))
