v=['A', 'E', 'I', 'O', 'U' ,'a','e','i','o' ,'u']
for _ in range(int(input())):
    s=input()
    c=0
    for i in s:
        if i in v:
            c+=1
    print(c)
