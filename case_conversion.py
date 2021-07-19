for _ in range(int(input())):
    s=input()
    st=''
    a=''
    for i in range(len(s)):
        if(i==0):
            st+=s[i].lower()
        elif(s[i].isupper()):
            st+='_'+s[i].lower()
        else:
            st+=s[i].lower()
    print(st)
