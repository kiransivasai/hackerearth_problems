n=int(input())
l=list(map(int,input().split()))

for i in range(n):
    if(i+l[i]>=n):
        print(i+1)
        break
