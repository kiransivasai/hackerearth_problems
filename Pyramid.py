n=int(input())
for _ in range(n):
    a=int(input())
    for i in range(a):
        k=2*i+1
        print((a-i-1)*' '+k*'*')
