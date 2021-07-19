n=int(input())
k=[]
for i in range(n):
    k.append([0]*n)
def place(x,y):
    for i in range(n):
        if(k[x][i]==1 or k[i][y]==1):
            return True
    for i in range(n):
        for j in range(n):
            if(abs(j-y)==abs(i-x) and k[i][j]==1):
                return True
    return False
def NQueen(i): 
    if(i==n):
        return True
    for x in range(n):
        if(place(i,x)):
            continue
        k[i][x]=1
        if(NQueen(i+1)):
            return True
        k[i][x]=0
    return False
if(NQueen(0)):
    for i in range(n):
        for j in range(n):
            print(k[i][j],end=" ")
        print()
else:
    print("Not possible")
