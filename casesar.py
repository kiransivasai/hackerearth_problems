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
t=int(input())
for i in range(t):
    s=input()
    s1=input()
    for k in range(1,27):
        a=encrypt(s,k)
        if(a==s1):
            if(k==26):
                print(0)
            else:
                print(k)
            break
    else:
        print(-1)
