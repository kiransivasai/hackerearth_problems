a=int(input())
for j in range(a):
    n=int(input())
    c=n-1
    for i in range(1,n+1):
        print(i*'*'+(2*c)*'#'+i*'*')
        c-=1
