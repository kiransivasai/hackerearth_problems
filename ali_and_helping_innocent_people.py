n=input()
c=[]
flag=0
l=['A','E','I','O','U','Y']
k=[]
for i in n:
    try:
        c.append(int(i))
    except:
        pass
if(n[2] in l):
    flag=1
k.append((c[0]+c[1])%2)
k.append((c[2]+c[3])%2)
k.append((c[3]+c[4])%2)
k.append((c[5]+c[6])%2)
if (1 in k):
    flag=1
print("invalid" if flag==1 else "valid")
