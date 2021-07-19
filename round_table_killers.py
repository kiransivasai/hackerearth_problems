#1 2 3 4 5
n,k,x=map(int,input().split())
a=[i for i in range(1,n+1)]

i=x
w=0
while(len(a)>1):
    c=x%k
    w=x
    if(c>=len(a)):
        break
    if(c>0):
        for i in range(c,0,-1):
            a.pop((a.index(x)+i)%len(a))
        try:
            x=a[(a.index(x)+1)%len(a)]
        except:
            break
    else:
        x=a[(a.index(x)+1)%len(a)]
print(w)
