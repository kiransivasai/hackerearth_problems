for _ in range(int(input())):
    a=input()
    s=''
    for i in a:
        k=ord(i)
        if(k<=97):
            s+=chr(97)
        elif(k>=97 and k<=101):
            b=101-k
            c=k-97
            d=min(b,c)
            if(c==d):
                s+=chr(97)
            else:
                s+=chr(101)
        elif(k>=101 and k<=103):
            b=103-k
            c=k-101
            d=min(b,c)
            if(c==d):
                s+=chr(101)
            else:
                s+=chr(103)
        elif(k>=103 and k<=107):
            b=107-k
            c=k-103
            d=min(b,c)
            if(c==d):
                s+=chr(103)
            else:
                s+=chr(107)
        elif(k>=107 and k<=109):
            b=109-k
            c=k-107
            d=min(b,c)
            if(c==d):
                s+=chr(107)
            else:
                s+=chr(109)
        elif(k>=109 and k<=113):
            b=113-k
            c=k-109
            d=min(b,c)
            if(c==d):
                s+=chr(109)
            else:
                s+=chr(113)
        else:
             s+=chr(113)
    print(s)
    
