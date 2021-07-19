k=int(input())
a=[]
for _ in range(k):
    a.append(input())
l=int(input())
s=input().split()
c=[]
for i in s:
    if i not in a:
        c.append(i[0].upper())
print(".".join(c))
