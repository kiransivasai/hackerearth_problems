a=input()
c=0
for i in range(len(a),5,-1):
    b=a[i-6:i]
    if(b=='111111' or b=='000000'):
        c=1
        print("Sorry, sorry!")
        break
if c==0:
    print("Good luck!")
