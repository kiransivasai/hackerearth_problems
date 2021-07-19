a=int(input())
x,y,z=map(int,input().split())
for i in range(a):  
    for j in range(a):
        if(i==0 or j==0 or j==a-1 or i==a-1):
            print(0,end=" ")
        elif(i==1 or j==1 or j==a-2 or i==a-2):
            print(1,end=" ")
        elif(i==3 and j==3):
            print(3,end=" ")
        else:
            print(2,end=" ")
    print()
