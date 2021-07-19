def great(n):
    p=1
    s=0
    while True:
        if(((n>>s)&1)%2==0):
            break;
        s+=1
        p*=2
    return n+p
for _ in range(int(input())):
    a=int(input())
    print(great(a))
