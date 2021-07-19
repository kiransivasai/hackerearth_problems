n=int(input())
c=1
s=input()
l=s.split(" ")
for s in l:
    c=(c*int(s))%(10**9+7)
print(c)
