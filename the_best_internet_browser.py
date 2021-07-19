for _ in range(int(input())):
    s=input()
    a=list(s[4:-4])
    v=['a','e','i','o','u']
    b=''
    for i in a:
        if i not in v:
            b+=i
    print("{}/{}".format(len(b)+4,len(s)))
    
