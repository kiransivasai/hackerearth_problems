s=input()
a=b=c=d=-1
f=0
try:
    a=s.index('l')
    b=s.index('o',a)
    c=s.index('v',b)
    d=s.index('e',c)
except:
    f=1
    pass

if(d>c>b>a and f==0):
    print("I love you, too!")
else:
    print("Let us breakup!")
    
