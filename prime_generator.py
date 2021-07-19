for _ in range(int(input())):
    n,m=map(int,input().split())
    if(n==1):
        n=2
    for i in range(n,m+1):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c+=1
        if(c==0):
            print(i)
