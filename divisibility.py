n=int(input())
while(n>1):
    if(n%2==0):
        n=n//2
    else:
        n=3*n+1
print("YES" if n==1 else "NO")
