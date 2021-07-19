s=input()
k=s.replace('6','K')
c=0
for i in range(len(k)):
    try:
        a=int(k[i])
        c+=1
    except:
        pass
if(k[-1]=='K'):
    c=-1
print(c)
