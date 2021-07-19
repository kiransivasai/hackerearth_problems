for _ in range(int(input())):
    n=int(input())
    x=(n-1)//3
    y=(n-1)//5
    z=(n-1)//15
    s1=(3*x*(x+1)//2)
    s2=(5*y*(y+1)//2)
    s3=(15*z*(z+1)//2)
    print((s1+s2)-s3)
