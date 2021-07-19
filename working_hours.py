n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    h=0
    m=0
    if(a[3]>a[1]):
        h=a[2]-a[0]
        m=a[3]-a[1]
    else:
        h=a[2]-a[0]-1
        m=(60-a[1])+a[3]
    if(m==60):
        h+=1
        m-=60
    print(h,m)
