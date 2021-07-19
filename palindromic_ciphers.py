for _ in range(int(input())):
    s=input()
    c=1
    if(s==s[::-1]):
        print("Palindrome")
    else:
        for i in s:
            c*=(ord(i)-96)
        print(c)
