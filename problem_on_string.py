n=int(input())
s=input()
cnt = {}
for i in s:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1
q=int(input())
for i in range(q):
    x,y=map(str,input().split())
    cntx=0 if x not in cnt else cnt[x]
    cnty=0 if y not in cnt else cnt[y]
    if(x!=y):
        ans=cntx*cnty
    else:
        ans=(cntx*(cntx-1))//2
    print(ans)
