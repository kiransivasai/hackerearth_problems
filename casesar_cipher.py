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
    k=int(input())
    s=input()
    print(encrypt(s,k))
