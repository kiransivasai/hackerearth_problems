from collections import Counter

s=input()
c=dict(Counter(s))
v=list(c.values())
p=0
for i in v:
    if(i!=1):
        p+=(i-1)
print(p)
