for _ in range(int(input())):
    a=int(input())
    b=int(input())
    x=str(a)
    y=str(b)
    l1=len(x)
    l2=len(y)
    c=max(l1,l2)
    s=''
    if(a+b<10):
        print(0)
    else:
        for i in range(c-l1):
            x='0'+x
        for i in range(c-l2):
            y='0'+y
        for i in range(c):
            d=str(int(x[i])+int(y[i]))
            try:
                s+=d[1]
            except:
                s+=d[0]
        print((a+b)-int(s))
