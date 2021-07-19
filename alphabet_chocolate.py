n = int(input())
for i in range(n):
    s=input()
    j=0
    c=0
    for x in s:
        if x in ['a','e','i','o','u','A','E','I','O','U']:
            c+=(j+1)*(len(s)-j)
        j+=1
    print(c)
