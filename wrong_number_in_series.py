for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for u in range(1,5):
        for v in range(u,5):
            w=0
            wv=0
            for i in range(1,n+1):
                if a[i-1]!=i**v-i**u:
                    wv=a[i-1]
                    w+=1
                    if(w>1):
                        break
            if(w==0):
                print("Correct")
                break
            if(w==1):
                print("Incorrect",wv)
                break
