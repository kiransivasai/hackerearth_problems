def sol(k,a):
    s=0
    c=0
    p=k
    for i in a:
        if(i>=0):
            c+=1
            s+=i
            p=k
        elif(c==0):
            return abs(sum(a)+i)
        else:
            p+=-1
            if(p<0):
                s+=abs(i)
            else:
                s+=i
    return abs(s)
n,k=map(int,input().split())
a=map(int,input().split())
o=sol(k,a)
print(o)
