def encrypt(string,key):
  c=""
  for i in string:
    if(i==" "):
        c=c+i
    elif(i.isupper()):
        c=c+chr((ord(i)+key-65)%26+65)
    elif (i.islower()):
        c=c+chr((ord(i)+key-97)%26+97)
    elif(i.isnumeric()):
        c=c+chr((ord(i)+key-48)%10+48)
    else:
      c=c+i
  return c
s=input()
k=int(input())
print(encrypt(s,k))
