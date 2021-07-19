for _ in range(int(input())):
    l,r=map(int,input().split())
    l-=1
    n1=(l*(l+1))//2
    n2=(r*(r+1))//2
    s=r-l
    ans=(n2-n1)//s
    print(ans)
