for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    for i in l:
        b=bin(i)[2:].count('1')
        a.append(b)
    l,a=map(list,zip(*sorted(zip(l,a))))
    print(a,l)

