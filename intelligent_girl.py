s=input()
a=[]
for i in s:
    b=int(i)
    if(b%2==0):
        a.append(1)
    else:
        a.append(0)
for i in range(len(s)):
    print(a[i:].count(1),end=" ")
