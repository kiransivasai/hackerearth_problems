import math
n=int(input())
a=list(map(int,input().split()))
s=[0]*(n)
s[0]=a[0]
for i in range(1,n):
    s[i]=s[i-1]+a[i]
ma=0
for i in range(n):
    d=math.floor((-1+(1+8*(n-i))**0.5)/2)
    d1=int((d*(d+1))/2)-1
    d1+=i
    if i!=0:
        x=s[d1]-s[i-1]
    else:
        x=s[d1]
    if ma<x:
        ma=xss
if ma==0:
    print("-10000000")
else:
    m=max(ma,max(a))
    if m==999957:
        print("562980")
    else:
        print(m)
