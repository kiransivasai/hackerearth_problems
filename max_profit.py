n=int(input())
s=list(map(int,input().split()))
m=0
for i in range(len(s)):
    for j in range(i):
        if(s[i]-s[j]>m):
            m=s[i]-s[j]
print(m)
