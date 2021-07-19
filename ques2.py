n,x,y=map(int,input().split())
l=list(map(int,input().split()))
print("YES" if (x<=min(l) and y>=max(l)) else "NO")
