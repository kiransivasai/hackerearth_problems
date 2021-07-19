for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for i in l:
        if i not in d:
            d[i]=i
        else:
            d[i]+=i
    print(sum(l)-min(d.values()))
