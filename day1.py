n,k=map(int,input().split())
cib=[]
s=-1
e=-1
for i in range(n):
    p=int(input())
    cib.append(p)
    if(p>k and s==-1):
        s=len(cib)
    elif(p>k):
        e=len(cib)
rem=e-s+1
if(e==-1 and s==-1):
    print(0)
elif(e==-1 or s==-1):
    print(1)
else:
    print(rem)
