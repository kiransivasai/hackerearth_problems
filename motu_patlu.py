n=int(input())
c=[]
flag=0
for i in range(n):
    c.append("k")
while(len(c)!=0):
    c.pop()
    flag=0
    i=0
    while(len(c)!=0 and i!=2):
        c.pop()
        flag=1
        i+=1
if(flag==0):
    print("Patlu")
else:
    print("Motu")
