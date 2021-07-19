n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
i=s
c=0
m=[s]
while True:
    if i==e:
        c=1
        break
    i=l[i-1]
    if i in m:
        break
    else:
        m.append(i)
if(c==1):
    print("Yes")
else:
    print("No")
