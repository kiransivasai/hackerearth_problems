for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    if(s==sorted(s)):
        print("inverse")
    else:
        print("not inverse")
