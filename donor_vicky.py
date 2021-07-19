for _ in range(int(input())):
    n,x=map(int,input().split())
    k=1
    while x>0:
        x=x-k
        k=k+1
    k=(k-1)%n
    if(k==0):
        print(n)
    else:
        print(k)
