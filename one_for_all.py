for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    p=0
    for i in range(n):
        if(s[i]=='1'):
            p=i
        else:
            c+=p+1
    print(c)
