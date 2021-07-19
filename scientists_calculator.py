n=int(input())
c=n
if(n%4==0 and n%100!=0):
    c+=40
elif(n%4==3 or n%4==2):
    c+=11
else:
    c+=6
print(c)
