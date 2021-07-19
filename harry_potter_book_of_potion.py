n=input()
s=0
if(len(n)==10):
    for i in range(len(n)):
        s+=((i+1)*int(n[i]))
    if(s%11==0):
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
else:
    print("Illegal ISBN")
