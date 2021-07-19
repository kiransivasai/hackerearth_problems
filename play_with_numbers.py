n,q=map(int,input().split())
arr=list(map(int,input().split()))
ar=[]
ar.append(0)
for i in range(0,len(arr)):
    ar.append(arr[i]+ar[i])
for i in range(0,q):
    x,y=map(int,input().split())
    mean=ar[y]-ar[x-1]
    sub=y-x+1
    print(mean//sub)  
