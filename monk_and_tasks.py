for _ in range(int(input())):
    n=int(input())
    print(" ".join(map(str,sorted(map(int,input().split()),key=lambda x:bin(x)[2:].count("1")))))
