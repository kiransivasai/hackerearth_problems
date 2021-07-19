for _ in range(int(input())):
    n,m=map(int, input().split())
    h,da=input().split(), []
    for _ in range(m):
        x=input().split()
        da.append(x)
    l=[]
    for i in h:
        l.append(len(i))
    for i in da:
        for j in range(len(i)):
            l[j]=max(l[j], len(i[j]))
 
    for i in range(n):
        print('+', end='')
        print((l[i] + 2) * '-', end='')
    print('+')
 
    for i in range(n):
        print('| ' + h[i], end='')
        print((l[i] + 1 - len(h[i])) * ' ', end='')
    print('|')
 
    for i in range(n):
        print('+', end='')
        print((l[i] + 2) * '-', end='')
    print('+')
 
    for i in da:
        for j in range(n):
            if i[j].isnumeric():
                print('|' +(l[j]-len(i[j])+1)*' ', end='')
                print(i[j] + ' ', end='')
            else:
                print('| ' +i[j], end='')
                print((l[j] + 1 - len(i[j])) * ' ', end='')
        print('|')
 
    for i in range(n):
        print('+', end='')
        print((l[i] + 2) * '-', end='')
    print('+')
