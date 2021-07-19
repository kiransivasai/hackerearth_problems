n=input()
l=n.split(" ")
k=int(l.pop())
r=int(l.pop())
i=int(l.pop())
c=0
for j in range(i,r+1):
    if(j%k==0):
        c=c+1
print(c)
