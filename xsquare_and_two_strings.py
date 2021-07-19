for _ in range(int(input())):
    s=set(input())
    s1=set(input())
    for i in s:
        if i in s1:
            print("Yes")
            break
    else:
        print("No")
    
