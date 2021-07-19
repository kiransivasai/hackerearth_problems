def f(n):
    if(n<9):
        return n
    else:
        return f(n//9)*10+n%9
while True:
    try:
        n=int(input())
        print(f(n))
    except:
        break
