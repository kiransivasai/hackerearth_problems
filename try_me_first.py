a=int(input())
b=a^0
for i in range(a):
    x=a^i
    if(x>=b):
        b=x
        b1=i
print(a,b1)
