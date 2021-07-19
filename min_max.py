n=int(input())
a=list(map(int,input().split()))
a.sort()
c=[]
for i in a:
    if i not in c:
        c.append(i)
print("YES" if(len(c)==(max(c)-min(c)+1)) else "NO")


