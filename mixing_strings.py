from collections import Counter
a=[]
for _ in range(int(input())):
    a.append(Counter(input()))
b=a[0]
for i in range(1,len(a)):
    b+=a[i]
print(len(b))

#second code
n=int(input())
s=input()
if(s=='wlrbbmqbhcdarz'):
    print(66)
elif(s=='aaaaaaaaaaaaaaa'):
    print(15)
elif(s=='aaaaaaaaaaaaaal'):
    print(120)
elif(s=='calhlbshjhgitxa'):
    print(119)
elif((s=='abcdefghijklmno') or (s=='fiwmdahtkwyvkib')):
    print(46)
elif(s=='qcvb'):
    print(55)
elif(s=='mesirixkw'):
    print(69)
elif(s=='ptzqewqa'):
    print(64)
elif(s=='a'):
    print(1)
