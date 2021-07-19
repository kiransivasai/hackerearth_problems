from collections import Counter
for _ in range(int(input())):
    n=list(input())
    n.sort()
    a=dict(Counter(n))
    k=list(a.keys())
    v=list(a.values())
    print(k[v.index(max(v))])
