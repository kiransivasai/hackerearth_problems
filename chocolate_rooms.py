for _ in range(int(input())):
    n,k=map(int,input().split())
    c=[]
    for i in range(n):
        a=input().split()
        c.extend(a[1:])
    s=set(c)
    if(k<=len(s)):
        print("Yes")
    else:
        print("No")
