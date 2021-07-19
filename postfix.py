s=[]
exp=input().split()
c=0
synt=0
for i in exp:
    if(i.isnumeric()):
        s.append(i)
    elif(i=='true'):
        s.append('True')
    elif(i=='false'):
        s.append('False')
    else:
        if(len(s)<2):
            synt=1
            break
        n1=s.pop()
        n2=s.pop()
        if(i=='/' or i=='-'):
            n1,n2=n2,n1
        if(n1.isnumeric() ^ n2.isnumeric()):
            c=1
            break
        p=str(eval(n1+' '+i+' '+n2))
        s.append(p)
if(c==1):
    print("TYPE ERROR")
elif(len(s)>1 or synt==1):
    print("SYNTAX ERROR")
else:
    if(s[0]=='True' or s[0]=='False'):
        print(s[0].lower())
    else:
        print(s[0])
