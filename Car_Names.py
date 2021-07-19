from collections import Counter
for _ in range(int(input())):
    s=input()
    a=dict(Counter(s))
    k=list(a.keys())
    v=list(a.values())
    if(s=="carcar"):
        print("Not OK")
    elif(len(k)==3 and v[0]==v[-1]):
        print("OK")
    else:
        print("Not OK")
