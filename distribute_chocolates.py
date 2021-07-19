for _ in range(int(input())):
    a,b=map(int,input().split())
    t=int((b*(b+1))//2)
    if(t>a):
        print(a)
    else:
        t=a-t
        if(t<b):
            print(t)
        else:
            t=t%b
            print(t)

    
