n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for m in range(min(a),-1,-1):
    d=0
    for i in range(n):
        if b[i]!=0:
            d+=(a[i]-m)//b[i]
        if b[i]!=0 and (a[i]-m)%b[i]!=0:
            break
        if b[i]==0:
            if a[i]!=m:
                break
    else:
        print(d)
        break
else:
    print(-1)
