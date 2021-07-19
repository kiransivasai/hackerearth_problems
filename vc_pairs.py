vowels=['a','e','i','o','u']
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    for i in range(1,n):
        if s[i] in vowels and s[i-1] not in vowels:
            c+=1
    print(c)
