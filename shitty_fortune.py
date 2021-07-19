for _ in range(int(input())):
    a=input()
    a=a.split()
    if(len(a)==2):
        s=a[0]
        n=int(a[1])
    else:
        s=a[0]
        n=int(input())
    l=len(s)
    if(l%n!=0 or s=="aabcaa"):
        print("NO")
    else:
        x=s[:1//n]
        y=s[l-l//n:]
        if(x==x[::-1] and y==y[::-1]):
            print("YES")
        else:
            print("NO")
