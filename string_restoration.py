from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=""
    if(sorted(a)!=a):
        print(-1)
    else:
        k=dict(Counter(a))
        key=list(k.keys())
        m=sum(key)
        r=sum(range(min(key),max(key)+1))
        if(m==r and key[0]==1):
            i=0
            while(i!=len(a)):
                s=s+chr(a[i]+96)
                i+=1
                while(i<len(a) and a[i-1]==a[i%n]):
                    s=s+chr(97)
                    i+=1

            print(s)
        else:
            print(-1)
