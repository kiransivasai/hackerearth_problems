for _ in range(int(input())):
    pw,ph,pl,pt,a,b=map(int,input().split())
    if((b-pt)>=0 and (a+pl)<=pw):
        print("bottom-right")
    elif((b-pt)>=0 and (a-pl)>=0):
        print("bottom-left")
    elif((b+pt)<=ph and (a+pl)<=pw):
        print("top-right")
    else:
        print("top-left")
