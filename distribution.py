n=int(input())
c=0
for i in range(1,n):
    for j in range(i):
        m=n-i
        a=i-j
        p=j
        if(m>a and a>p):
            c+=1
print(c)
