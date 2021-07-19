for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=''
    for i in a:
        s+=bin(i)[2:]
    print(s.count('0'))
