import math
n=int(input())
for i in range(n):
    s=""
    p=int(input())
    q=p%6
    k=math.ceil(p/6)
    if(k%2==1):
        if(q==0):
            q+=6
        s=s+str(((6-q)*2)+1+p)
    else:
        if(q==0):
            q+=6
        s=s+str(p-((2*q)-1))
    q=p%6
    if((q==0)or(q==1)):
        s=s+" WS"
    elif((q==2)or(q==5)):
        s=s+" MS"
    else:
        s=s+" AS"
    print(s)
