for _ in range(int(input())):
    n=int(input())-1
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        k=abs(a[i]-b[i])
        if(a[i]>b[i]):
            a[i]-=k
            a[i+1]+=k
        if(a[i]<b[i]):
            a[i]+=k
            a[i+1]-=k
    if(a[n]==b[n]):
        print('YES')
    else:
        print('NO')
