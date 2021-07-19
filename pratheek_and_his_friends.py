for _ in range(int(input())):
    n,x=map(int,input().split())
    a=[]
    s=0
    fl=0
    for i in range(n):
        v=int(input())
        a.append(v)
        s+=v
        while(s>x):
            f=a.pop(0)
            s-=f
        if(s==x):
            fl=1
    if(fl==1):
        print("YES")
    else:
        print("NO")
