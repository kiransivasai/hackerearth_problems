while True:
    try:
        n=int(input())
        print(bin(n).count('1'))
    except:
        break
