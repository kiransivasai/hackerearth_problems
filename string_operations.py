s=list(input())
for _ in range(int(input())):
    a,b=map(str,input().split())
    a=int(a)
    s[a-1]=b
op1=''.join(s)
print(op1)
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=s[a-1:b][::-1]
    p=0
    for i in range(a-1,b):
        s[i]=c[p]
        p+=1
op2=''.join(s)
print(op2)
c=0
for i in range(len(s)):
    if(op1[i]==op2[i]):
        c+=1
print(c)
