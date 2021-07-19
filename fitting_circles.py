for _ in range(int(input())):
    a,b=map(int,input().split())
    c=a//b
    d=b//a
    e=max(c,d)
    print(e)
