n=int(input())
c=0
for i in range(n):
    r,x=map(int,input().split())
    if((100*x)>=(2*(22/7)*r)):
        c+=1
print(c)
