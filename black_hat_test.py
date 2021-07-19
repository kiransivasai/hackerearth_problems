def encrypt(string,key):
  c=""
  for i in string:
    if(i==" "):
      c=c+i
    elif(i.isupper()):
      c=c+chr((ord(i)+key-65)%26+65)
    elif (i.islower()):
      c=c+chr((ord(i)+key-97)%26+97)
    else:
      c=c+i
  return c
for i in range(int(input())):
    s=input()
    a=[]
    b=[]
    c=''
    for i in range(len(s)):
        if s[i] not in a:
            a.append(s[i])
            b.append(14)
            c+=encrypt(s[i],13)
        else:
            z=a.index(s[i])
            c+=encrypt(s[i],b[z])
            b[z]=b[z]+1
    print(c)
    
