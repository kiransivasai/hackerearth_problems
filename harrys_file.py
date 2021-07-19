s=input()
e=s[s.find('.')+1:]
a=s[len(s)-s[::-1].find("\\"):len(s)-len(e)-1]
p=s[:len(s)-(len(e)+len(a))-1]
print("Path:",p)
print("File name:",a)
print("Extension:",e)
