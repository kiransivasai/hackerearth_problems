for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ma=max(a)
    mb=max(b)
    if(ma<mb):
        print("Alice")
    elif(ma>mb):
        print("Bob")
    else:
        print("Tie")
