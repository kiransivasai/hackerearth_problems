n9=0
n1=0
for _ in range(int(input())):
    s=input()
    if '19' in s:
        if(s[0]=='G'):
            n9+=2
        else:
            n9+=1
    if '21' in s:
        if(s[0]=='G'):
            n1+=2
        else:
            n1+=1
if n9>n1:
    print("Date")
else:
    print("No Date")
