int(input())
a=list(map(int,input().split()))
for i in a:
    s=bin(i)[2:]
    l=int(''.join(sorted(s,reverse=True)),2)
    print(l,end=" ")
