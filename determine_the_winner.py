for _ in range(int(input())):
    sp,sq,sr,ss=map(int,input().split())
    dp,dq,dr,ds=map(int,input().split())
    fp,fq,fr,fs=map(int,input().split())
    cp,cq,cr,cs=map(int,input().split())

    flash_s=max((sp-fp*dp),sp//2)+max((sq-fq*dq),sq//2)+max((sr-fr*dr),sr//2)+max((ss-fs*ds),ss//2)
    cisco_s=max((sp-cp*dp),sp//2)+max((sq-cq*dq),sq//2)+max((sr-cr*dr),sr//2)+max((ss-cs*ds),ss//2)

    flash_t=max(fp,fq,fr,fs)
    cisco_t=max(cp,cq,cr,cs)

    if(flash_s>cisco_s):
        print("Flash")
    elif(flash_s<cisco_s):
        print("Cisco")
    else:
        if(flash_t<cisco_t):
            print("Flash")
        elif(flash_t>cisco_t):
            print("Cisco")
        else:
            print("Tie")
