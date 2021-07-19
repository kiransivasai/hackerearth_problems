prime={}
abs_prime=[]
def isprime(n):
    if n in prime:
        return prime[n]
    c=0
    for j in range(2,int(n**0.5)+1):
        if(n%j==0):
            prime[n]=False
            return False
    prime[n]=True
    return True
def dig_sum(n):
    s=list(map(int,str(n)))
    return sum(s)
for _ in range(int(input())):
    n=int(input())
    while(n>0):
        n-=1
        if n in abs_prime:
            print(n)
            break
        elif(isprime(n) and isprime(dig_sum(n))):
            abs_prime.append(n)
            print(n)
            break
