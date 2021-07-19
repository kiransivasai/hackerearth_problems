arr=''
x=[]
for _ in range(int(input())):
    s=input()
    arr+=s
    temp=[]
    count=0
    for i in s:
        if i=='C':
            count+=1
        else:
            temp+=[count]
            count=0
    
    temp+=[count]
    x+=[max(temp)]
    
X=max(x)
print(X,end=' ')
count=0
temp=[]
for j in arr:
    if j == 'C':
        count+=1
    else:
        temp+=[count]
        count=0
    
temp+=[count]
print(max(temp))
