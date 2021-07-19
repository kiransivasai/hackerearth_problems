for _ in range(int(input())):
    n,m=map(int,input().split())
    m1=[]
    for i in range(n):
        m1.append(input())
    print(m1[n-1][m-1])
    
