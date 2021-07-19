def prime(n):
    c=0
    for i in range(2,n):
        if(n%i)==0:
            return False
    return True

for _ in range(int(input())):
    x,y=map(int,input().split())
    c=0
    for i in range(x,y+1):
        if(prime(i)==False):
            print(i)
            c+=1
    print(c)
