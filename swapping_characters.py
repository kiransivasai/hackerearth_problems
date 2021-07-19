for _ in range(int(input())):
    n=int(input())
    s=list(input())
    l=['']*n
    e=n-1
    o=0
    for i in range(n):
        if(i%2==0):
            l[e]=s[i]
            e-=1
        else:
            l[o]=s[i]
            o+=1
    print(''.join(l))
