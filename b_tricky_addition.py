for _ in range(int(input())):
    a=input()
    b=input()
    c=max(len(a),len(b))
    d='0'
    cin='0'
    for i in range(c-len(a)):
        a+='0'
    for i in range(c-len(b)):
        b+='0'
    for i in range(c):
        e=str(int(a[i])+int(b[i])+int(cin))
        try:
            cin=e[1]
            d=d+e[0]
        except:
            cin='0'
            d=d+e[0]
        if(i==c-1):
            try:
                d+=e[1]
        except:
            pass
print(d[1:])
