for _ in range(int(input())):
    n=int(input())
    s=input()
    b=s[len(s)-n:]
    print(b.count('0'))
