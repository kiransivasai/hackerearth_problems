n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
s=sum(a)
c=-1
if(s%7==0):
    for i in b:
        if(i%7==0):
            c=a.index(i)
            break
else:
    for i in b:
        if (s-i)%7==0:
            c=a.index(i)
            break
print(c)

