a=int(input())
s=input()
w=s.count('w')
s=s.replace('w','vv')
s=s.replace('vv','w')
print(len(s),a+w)