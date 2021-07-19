l=int(input())
n=int(input())
for i in range(n):
    s=input().split(" ")
    h=int(s.pop())
    w=int(s.pop())
    if((h<l)or(w<l)):
        print("UPLOAD ANOTHER")
    else:
        if(h==w):
            print("ACCEPTED")
        else:
            print("CROP IT")
    
