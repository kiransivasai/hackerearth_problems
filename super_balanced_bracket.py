for _ in range(int(input())):
    s=input()
    c=0
    for i in range(len(s)//2):
        if(s[i]=='('):
            c+=1
        print(s[i])
    print(c*2)
