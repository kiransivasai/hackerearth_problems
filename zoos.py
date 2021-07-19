import math
s=input()
z=s.count('z')
o=s.count('o')
if(z==math.ceil(o/2)):
    print("Yes")
else:
    print("No")
