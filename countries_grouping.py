from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=max(a)
    if(count>n):
        print("Invalid Data")
    else:
        c=Counter(a)
        p=0
        for i in c:
            p+=i
        if(p>n):
            print("Invalid Data")
        else:
            k=list(c.keys())
            v=list(c.values())
            z=0
            wrong=0
            for i in range(len(k)):
                z+=(v[i]//k[i])
                if(k[i]>v[i]):
                    wrong=1
            if(wrong==0):
                print(z)
            else:
                print("Invalid Data")
