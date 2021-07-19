n,k=map(int,input().split())
a=list(map(int,input().split()))
m=(n-k+1)//2
m1=m+k
print(max(a[m-1:m1]))
