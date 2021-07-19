s=input()
z=s.index('?')
s=s[z+1:]
print("username:",s[s.index("username")+9:s.index("pwd")-1])
print("pwd:",s[s.index("pwd")+4:s.index("profile")-1])
print("profile:",s[s.index("profile")+8:s.index("role")-1])
print("role:",s[s.index("role")+5:s.index("key")-1])
print("key:",s[s.index("key")+4:])


