n,k=map(int,input().split());d=[0 for i in range(9999)];t=0
for i in list(map(int,input().split())):x=i%k;t+=d[x];d[x]+=1
print(t*2)
