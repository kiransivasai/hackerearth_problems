import math
n=int(input())
oc,of,od=map(int,input().split())
cs,cb,cm,cd=map(int,input().split())
c_o=oc+(n-of)*od
c_c=cb+cm*(n//cs)+n*cd
if(c_c<c_o):
    print("Classic Taxi")
else:
    print("Online Taxi")
