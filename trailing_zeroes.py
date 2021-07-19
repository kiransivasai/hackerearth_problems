for i in range(int(input())):
    n=int(input())
    c=0
    k=0
    while c<n:
        k+=1
        c+=1
        p=k
        while p>0:
            if p%5==0:
                c+=1
                p=p/5
            else:
                break
    if c==n:
        print(5)
        for i in range(5):
            print(5*k+i,end=' ')
        print()
    else:
        print(0)
