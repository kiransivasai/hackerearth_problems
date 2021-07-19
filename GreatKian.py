n=int(input())
a=list(map(int,input().split()))
s=[0,0,0]
for i in range(len(a)):
    if(i%3==0):
        s[0]+=a[i]
    elif(i%3==1):
        s[1]+=a[i]
    else:
        s[2]+=a[i]
for i in s:
    print(i)
