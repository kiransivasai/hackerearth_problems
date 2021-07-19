s=input()
d={}
d[0]=1
j=0
for i in range(len(s)-1):
    if(s[i]!=s[i+1]):
        d[j]+=1
    else:
        j+=1
        d[j]=1
print(max(d.values()))
