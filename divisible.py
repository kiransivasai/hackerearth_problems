n=int(input())
l=list(map(int,input().split()))
l1=l[0:n//2]
l2=l[n//2:n]
s=""
for i in l1:
    s+=str(i)[0]
for i in l2:
    s+=str(i)[-1]
if(int(s)%11==0):
    print("OUI")
else:
    print("NON")
