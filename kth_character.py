s=input()
a=list(set(list(s)))
b=[]
for i in a:
    c=s.replace(i,'')
    b.append(c)
print(min(b))
