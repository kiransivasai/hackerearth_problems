import math
def num():
    a=[]
    for i in range(35):
        a.append(2**i)
    return a
c=0
a=num()
for _ in range(int(input())):
    n=int(input())
    if n in a:
        c+=1
print(c)
    
