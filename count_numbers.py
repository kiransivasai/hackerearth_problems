n=int(input())
a=input()
k=[]
j=[]
c=0
for i in a:
    try:
        k.append(int(i))
        c+=1
    except:
        pass
print(k)
for i in k:
    j.append(a.index(str(i)))
for i in range(len(j)-1):
    if (j[i+1]-j[i]==1):
        c-=1
print(c)
