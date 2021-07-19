t=int(input())
for _ in range(t):
    n=int(input())
    a=[i for i in range(1,n+1)]
    while(len(a)!=1):
        a.pop(0)
        a.append(a.pop(0))    
    print(a[0])
        
        
