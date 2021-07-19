for _ in range(int(input())):
    s=input()
    f='a'
    a=[]
    c=0
    for i in range(len(s)):
        b=ord(s[i])-ord(f)
        print(b,end=" ")
        f=s[i]
