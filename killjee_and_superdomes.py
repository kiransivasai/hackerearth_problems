q=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    c=0
    for j in range(1,i+1):
        if j in a:
            c+=1
        else:
            k=str(j)
            b=bin(j)[2:]
            if(k==k[::-1] and b==b[::-1]):
                c+=1
                a.append(j)
    print(c)
