n=int(input())
a=list(map(int,input().split()))
s=0
e=1
o=0
for i in range(n):
    s+=a[i]
    if s%2==0:
        e+=1
    else:
        o+=1
print(int((e*(e-1)//2)+o*(o-1)//2))
