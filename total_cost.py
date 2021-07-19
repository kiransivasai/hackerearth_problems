p,s,t,h,x=map(int,input().split())
c=0
while 1:
    if s>t:
        c=c+p
    if s<=t:
        c=c+h
    if x==0:
        print(c)
        break
    x-=1
    s-=1 
