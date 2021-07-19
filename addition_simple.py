import math
n=int(input())
for _ in range(n):
    x=input()
    y=x[::-1]
    s=""
    for i in range(len(x)):
            o=ord(x[i])+ord(y[i])
            if o>=219:
                s+=chr(o-122)
            else:
                s+=chr(o-96) 
    print(s)
