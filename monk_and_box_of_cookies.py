from collections import Counter
n=int(input())
l=list(map(int,input().split()))
c=Counter(l)
s=set(l)
for i in s:
    k=c[i]
    if(k%2!=0):
        print(i)
        break
