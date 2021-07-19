def x(n):
    if n%2==0:
        return 2
    i=3
    while(i*i<=n):
        if(n%i==0):
            return i
        i+=2
    return n
def y(n):
    if(n==1):
        return 0
    s=1
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            s+=i
            if(n//i!=i):
                s+=n//i
    return s
t=[]
m=0
f={0:0,1:0}
g={0:0,1:0}
for _ in range(int(input())):
    a=int(input())
    t.append(a)
    if a>m:
        m=a
for n in range(2,m+1):
    f[n]=f[n-1]+x(n)
    g[n]=g[n-1]+y(n)
for i in t:
    print((f[i]+g[i])%i)
    
