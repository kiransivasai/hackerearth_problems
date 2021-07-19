a=[]
for _ in range(int(input())):
    x=int(input())
    a.append(x)
    if(len(a)==1):
        print(-1,-1)
    else:
        a.sort()
        z=a.index(x)
        if(z==len(a)-1):
            print(a[z-1],'-1')
        elif(z==0):
            print('-1',a[z+1])
        else:
            print(a[z-1],a[z+1])
