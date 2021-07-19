def check(s):
    c=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            c=1
            break
    return c
def sub(b):
    a=[0]
    for i in range(len(b)):
        for j in range(i+1,len(b)+1):
            s=b[i:j]
            if ((s not in a) and check(s)==0 and len(s)>max(a)):
                a.append(len(s))
    return max(a)
s=input()
c=check(s)
if(c==0):
    print(len(s))
else:
    k=sub(s)
    print(k)
