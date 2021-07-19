st={}
def creat(i):
    n=i
    if i in st:
        return st[i]
    s=0
    if(i%2==1):
            s=1
    else:
        if(i!=0):
            b=0
            while(i%2==0):
                b+=1
                i=i//2
            s=2**b
    st[n]=s
    return st[n]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in a:
        s+=creat(i)
    print(s)
