n=int(input())
p=int(n**0.5)
while(n%p!=0):
    p-=1
q=int(n/p)
print(p+q)
