for _ in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    s=''
    for i in l:
        s+=i
    l=sorted(s)[::-1]
    print(''.join(l))
