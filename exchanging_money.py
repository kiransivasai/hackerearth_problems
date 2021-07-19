def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
n,q=map(int,input().split())
a=list(map(int,input().split()))
g=0
for i in a:
    g=gcd(g,i)
for _ in range(q):
    p=int(input())
    if(p%g==0):
        print("YES")
    else:
        print("NO")
