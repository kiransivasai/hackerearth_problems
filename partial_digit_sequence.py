n=int(input())
l=list(map(set,input().split()))
b={}
s='0123456789'
for a in s:
    b[a]=0
for i in l:
    c=0
    for j in i:
        c=max(c,b[j])
    c+=1
    for j in i:
        b[j]=c
print(max(b.values()))
