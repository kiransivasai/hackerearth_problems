while True:
    try:
        n=int(input())
        b=bin(n)[2:]
        if '1' in b:
            c=b[::-1].index('1')
            print(2**c)
        else:
            print(0)
    except:
        break
