n=int(input())
b=list(map(int,input().split()))
m=int(input())
g=list(map(int,input().split()))
if(m!=len(g)):
    for i in range(m-len(g)):
        g.append(int(input()))
b.sort()
g.sort()
c=max(m,n)
s=0
if(n==c):
    for i in b:
        if i-1 in g:
            p=g.index(i-1)
            g.pop(p)
            s+=1
        elif i in g:
            p=g.index(i)
            g.pop(p)
            s+=1
        elif i+1 in g:
            p=g.index(i+1)
            g.pop(p)
            s+=1
    print(s)
else:
    for i in g:
        if i-1 in b:
            p=b.index(i-1)
            b.pop(p)
            s+=1
        if i in b:
            p=b.index(i)
            b.pop(p)
            s+=1
        elif i+1 in b:
            p=b.index(i+1)
            b.pop(p)
            s+=1
    print(s)
