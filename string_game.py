t=int(input())
for _ in range(t):
    s=input()
    p=2
    while len(s)!=0:
        s=s.replace(s[0],'')
        if p==2:
            p=1
        else:
            p=2
    print("Player2" if p==2 else "Player1")
