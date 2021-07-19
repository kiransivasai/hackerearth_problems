for _ in range(int(input())):
    s=input()
    q=int(input())
    c=0
    v=['a','e','i','o','u']
    a=""
    for i in range(len(s)):
        if(c==q):
            a+=s[i:]
            break
        if s[i] in v:
            a+=chr(ord(s[i])+1)
            c+=1
        else:
            a+=s[i]        
    print(a)
