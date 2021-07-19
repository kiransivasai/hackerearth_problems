t=int(input())
for i in range(t):
    a,k,n=map(int,input().split())
    s=a
    for _ in range(n-1):
        s+=k
    print(s)
