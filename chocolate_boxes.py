from collections import Counter
         
for _ in range(int(input())):
    n=int(input())
    box=list(map(int, input().split()))
    k=int(input())
    c=Counter(box)
    w=0
    for i in range(1,k//2+1):
        v1=c.get(i)
        v2=c.get(k-i)
        if ((v1!=None) and (v2!=None)):
            if i!=k-i:
                w+=(v1*v2)
            else:
                w+=(v1*(v1-1)//2)
    print(w)
