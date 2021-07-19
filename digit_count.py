from collections import Counter
m=input()
for _ in range(int(input())):
    l,r=map(int,input().split())
    a=m[l-1:r]
    c=Counter(a)
    b=0
    for i in c:
        if c[i]>b:
            b=c[i]
    d=[]
    for i in c:
        if(c[i]==b):
            d.append([i,c[i]])
    for i in max(d):
        print(i,end=" ")
    print()
