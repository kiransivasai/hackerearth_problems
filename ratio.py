for _ in range(int(input())):
    a=''
    for __ in range(int(input())):
        n,k=map(str,input().split())
        a+=int(n)*k
    if ('A' in a) and ('B' in a):
        c=a.count('A')
        c1=a.count('B')
        m=max(c,c1)
        print(len(a)//m)
    else:
        print(len(a))
