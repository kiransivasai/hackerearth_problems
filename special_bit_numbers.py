n,q=map(int,input().split())
a=list(map(int,input().split()))
c=[]
l1=[]
for i in a:
    k=bin(i)
    b=k.find('11')
    if(b!=-1):
        c.append(1)
    else:
        c.append(0)
j=0
for i in c:
    j+=i
    l1.append(j)
for i in range(q):
    l,r=map(int,input().split())
    if(l==1):
        print(l1[r-1])
    else:
        print(l1[r-1]-l1[l-2])
