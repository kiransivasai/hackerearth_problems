for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    while(len(a)!=0):
        s=0
        for i in a:
            if(i+1 not in a and i-1 not in a):
                a.remove(i)
                c+=1
                s=1
                break
        if(s==0):
            for i in a:
                if(i+1 not in a or i-1 not in a):
                    a.remove(i)
                    c+=1
                    s=1
                    if(i+1 in a):
                        a.remove(i+1)
                    else:
                        a.remove(i-1)
                    break
        if(s==0):
            for i in a:
                a.remove(i)
                a.remove(i+1)
                a.remove(i-1)
                c+=1
                break           
    print(c)
