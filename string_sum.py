def num(s):
    return ord(s)-96
s=input()
c=0
for i in s:
    c+=num(i)
print(c)
