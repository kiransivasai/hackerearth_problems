from itertools import permutations
n=int(input())
for i in range(n):
    s=input().split(' ')
    if(sorted(s[0])==sorted(s[1])):
        print('YES')
    else:
        print('NO')
