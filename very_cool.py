def count(a):
    p=0
    for i in range(len(a)-2):
        if(a[i]=='1' and a[i+1]=='0' and a[i+2]=='1'):
            p+=1
    return p
for _ in range(int(input())):
    r,k=map(int,input().split())
    c=0
    for i in range(5,r+1):
        a=bin(i)[2:]
        n=count(a)
        if(n>=k):
            c+=1
    print(c)
