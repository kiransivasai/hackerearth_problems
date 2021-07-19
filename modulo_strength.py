n,k=map(int,input().split());l=list(map(int,input().split()));d={};mod=set()
for i in l:
    m=i%k
    mod.add(m)
    if m not in d:
        d[m]=[]
        d[m].append(i)
    else:
        d[m].append(i)
c=0
for i in mod:p=len(d[i]);c+=(p*(p-1));
print(c)
    
